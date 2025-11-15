# transactions/views.py

import json
import logging
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import transaction
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.generic import (
    DetailView, ListView, CreateView, UpdateView, DeleteView
)

# Models
from .models import Sale, SaleDetail, Purchase
from store.models import Item
from accounts.models import Customer

# Forms
from .forms import PurchaseForm

logger = logging.getLogger(__name__)


# ----------------------------
# Utility
# ----------------------------
def is_ajax(request):
    return request.headers.get("X-Requested-With") == "XMLHttpRequest"


# ----------------------------
# SALES LIST VIEW
# ----------------------------
class SaleListView(ListView):
    model = Sale
    template_name = "transactions/sales_list.html"
    context_object_name = "sales"
    paginate_by = 20

    def get_queryset(self):
        return Sale.objects.all().order_by("-date_added")


class SaleDetailView(DetailView):
    model = Sale
    template_name = "transactions/saledetail.html"


# ----------------------------
# SALE CREATE VIEW (FINAL WORKING VERSION)
# ----------------------------
@require_http_methods(["GET", "POST"])
def SaleCreateView(request):

    # GET → Render page
    if request.method == "GET":
        context = {
            "active_icon": "sales",
            "customers": [c.to_select2() for c in Customer.objects.all()],
            "items": [i.to_select2() for i in Item.objects.all()],
        }
        return render(request, "transactions/salecreate.html", context)

    # POST → Process submitted form (non-AJAX)
    try:
        items_json = request.POST.get("items", "[]")
        customer_id = request.POST.get("customer")

        amount_paid = float(request.POST.get("amount_paid") or 0)
        tax_percentage = float(request.POST.get("tax_percentage") or 0)

        items_list = json.loads(items_json)
        if len(items_list) == 0:
            raise ValueError("No items added to sale.")

        # Create Sale
        sale = Sale.objects.create(
            customer_id=customer_id if customer_id else None,
            tax_percentage=tax_percentage,
            amount_paid=amount_paid,
            date_added=timezone.now(),
        )

        subtotal = 0.0

        # Create each sale detail entry
        for it in items_list:
            item_obj = Item.objects.get(pk=int(it["id"]))
            qty = int(it.get("quantity", 1))
            price = float(it.get("price", item_obj.price))
            total_detail = qty * price

            SaleDetail.objects.create(
                sale=sale,
                item=item_obj,
                price=price,
                quantity=qty,
                total_detail=total_detail,
            )

            # Deduct stock
            item_obj.quantity = max(0, item_obj.quantity - qty)
            item_obj.save()

            subtotal += total_detail

        tax_amount = (subtotal * tax_percentage) / 100
        grand_total = subtotal + tax_amount
        change = amount_paid - grand_total

        sale.sub_total = subtotal
        sale.tax_amount = tax_amount
        sale.grand_total = grand_total
        sale.amount_change = change
        sale.save()

        messages.success(request, "Sale created successfully.")
        return redirect("saleslist")

    except Exception as e:
        messages.error(request, f"Sale failed: {e}")
        return redirect("salecreate")


# ----------------------------
# SALE DELETE VIEW
# ----------------------------
class SaleDeleteView(DeleteView):
    model = Sale
    template_name = "transactions/saledelete.html"

    def get_success_url(self):
        return reverse("saleslist")


# ----------------------------
# EXPORT SALES TO EXCEL
# ----------------------------
from openpyxl import Workbook

def export_sales_to_excel(request):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = 'Sales'

    columns = [
        'ID', 'Date', 'Customer', 'Sub Total', 'Grand Total',
        'Tax Amount', 'Tax Percentage', 'Amount Paid', 'Amount Change'
    ]
    worksheet.append(columns)

    sales = Sale.objects.all()

    for sale in sales:
        worksheet.append([
            sale.id,
            sale.date_added.replace(tzinfo=None) if sale.date_added else '',
            sale.customer.phone if sale.customer else '',
            sale.sub_total,
            sale.grand_total,
            sale.tax_amount,
            sale.tax_percentage,
            sale.amount_paid,
            sale.amount_change,
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=sales.xlsx'
    workbook.save(response)
    return response


# ----------------------------
# PURCHASE VIEWS
# ----------------------------
class PurchaseListView(ListView):
    model = Purchase
    template_name = "transactions/purchases_list.html"
    context_object_name = "purchases"
    paginate_by = 10


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = "transactions/purchasedetail.html"


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "transactions/purchases_form.html"

    def get_success_url(self):
        return reverse("purchaseslist")


class PurchaseUpdateView(UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "transactions/purchases_form.html"

    def get_success_url(self):
        return reverse("purchaseslist")


class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = "transactions/purchasedelete.html"

    def get_success_url(self):
        return reverse("purchaseslist")
from openpyxl import Workbook

def export_purchases_to_excel(request):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = 'Sales'

    columns = [
        'ID', 'Date', 'Customer', 'Sub Total', 'Grand Total',
        'Tax Amount', 'Tax Percentage', 'Amount Paid', 'Amount Change'
    ]
    worksheet.append(columns)

    sales = Sale.objects.all()

    for sale in sales:
        worksheet.append([
            sale.id,
            sale.date_added.replace(tzinfo=None) if sale.date_added else '',
            sale.customer.phone if sale.customer else '',
            sale.sub_total,
            sale.grand_total,
            sale.tax_amount,
            sale.tax_percentage,
            sale.amount_paid,
            sale.amount_change,
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=sales.xlsx'
    workbook.save(response)
    return response
