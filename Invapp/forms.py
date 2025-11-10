from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }

        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder': 'Enter Product ID','class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter Product Name','class': 'form-control'}),
            'sku': forms.NumberInput(attrs={'placeholder': 'Enter Product SKU','class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter Product Price','class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Enter Product Quantity','class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'Enter Supplier Name','class': 'form-control'}),
        }