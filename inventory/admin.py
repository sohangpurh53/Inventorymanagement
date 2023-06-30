from django.contrib import admin
from .models import Sale, Product, Stock, Purchase
# Register your models here.
admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Purchase)