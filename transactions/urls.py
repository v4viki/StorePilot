from django.urls import path
from . import views

urlpatterns = [

    # ---------------------------
    # 🔹 SALES URLS
    # ---------------------------
    path("sales/", views.SaleListView.as_view(), name="saleslist"),
    path("sales/<int:pk>/", views.SaleDetailView.as_view(), name="saledetail"),
    path("sales/<int:pk>/delete/", views.SaleDeleteView.as_view(), name="saledelete"),

    # Create New Sale (function view)
    path("new-sale/", views.SaleCreateView, name="salecreate"),

    # ---------------------------
    # 🔹 PURCHASE URLS
    # ---------------------------
    path("purchases/", views.PurchaseListView.as_view(), name="purchaseslist"),
    path("purchases/<int:pk>/", views.PurchaseDetailView.as_view(), name="purchasedetail"),
    path("purchases/create/", views.PurchaseCreateView.as_view(), name="purchasecreate"),
    path("purchases/<int:pk>/update/", views.PurchaseUpdateView.as_view(), name="purchaseupdate"),
    path("purchases/<int:pk>/delete/", views.PurchaseDeleteView.as_view(), name="purchasedelete"),

    # ---------------------------
    # 🔹 EXPORT URLS
    # ---------------------------
    path("export/sales/", views.export_sales_to_excel, name="export_sales"),
    path("export/purchases/", views.export_purchases_to_excel, name="export_purchases"),

]
