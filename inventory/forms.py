from django import forms
from .models import Sale, Product,Purchase

class ProductForm(forms.ModelForm):
    class Meta:
       model = Product
       fields = '__all__'

class SaleForm(forms.ModelForm):
    class Meta:
       model = Sale
       fields = '__all__'


class PurchaseForm(forms.ModelForm):
    class Meta:
       model = Purchase
       fields = '__all__'