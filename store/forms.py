"""
Forms module for StorePilot store management application.

This module contains form definitions for:

- ItemForm: Form for creating and updating items/products
- CategoryForm: Form for creating and updating categories
- DeliveryForm: Form for creating and updating deliveries
"""

from django import forms
from .models import Item, Category, Delivery
from accounts.models import Vendor


class CategoryForm(forms.ModelForm):
    """
    Form for creating and updating Category instances.

    Fields:
    - name: Category name (required)
    - description: Category description (optional)
    """

    name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter category name'
        })
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter category description',
            'rows': 4
        })
    )

    class Meta:
        model = Category
        fields = ['name', 'description']


class ItemForm(forms.ModelForm):
    """
    Form for creating and updating Item instances.

    Fields:
    - name: Item name (required)
    - description: Item description (required)
    - category: Category the item belongs to (required)
    - quantity: Quantity in stock (required)
    - price: Item price (required)
    - expiring_date: Item expiration date (optional)
    - vendor: Vendor who supplies the item (required)
    """

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),  # ✅ All categories available
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        empty_label="Select a category"
    )

    vendor = forms.ModelChoiceField(
        queryset=Vendor.objects.all(),  # ✅ All vendors available
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        empty_label="Select a vendor"
    )

    name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter product name'
        })
    )

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter product description',
            'rows': 4
        })
    )

    quantity = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter quantity',
            'min': '0'
        })
    )

    price = forms.FloatField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter price',
            'min': '0',
            'step': '0.01'
        })
    )

    expiring_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        })
    )

    class Meta:
        model = Item
        fields = ['name', 'description', 'category', 'quantity', 'price', 'expiring_date', 'vendor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure querysets are always fresh and not filtered
        self.fields['category'].queryset = Category.objects.all()
        self.fields['vendor'].queryset = Vendor.objects.all()


class DeliveryForm(forms.ModelForm):
    """
    Form for creating and updating Delivery instances.

    Fields:
    - item: Item being delivered (optional)
    - customer_name: Name of the customer (optional)
    - phone_number: Customer's phone number (optional)
    - location: Delivery location (optional)
    - date: Delivery date and time (required)
    - is_delivered: Whether delivery has been completed (optional)
    """

    item = forms.ModelChoiceField(
        queryset=Item.objects.all(),  # ✅ All items available
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        empty_label="Select an item"
    )

    customer_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter customer name'
        })
    )

    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter phone number'
        })
    )

    location = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter delivery location'
        })
    )

    date = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        })
    )

    is_delivered = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    class Meta:
        model = Delivery
        fields = ['item', 'customer_name', 'phone_number', 'location', 'date', 'is_delivered']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure item queryset is always fresh
        self.fields['item'].queryset = Item.objects.all()
