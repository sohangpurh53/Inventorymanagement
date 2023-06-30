from django.contrib import admin
from django.urls import path, include
from inventory import views


urlpatterns = [
  path('', views.Homepage, name='Homepage'),
  path('product/', views.productpage, name='productpage'),
  path('sales/', views.salespage, name='salespage'),
  path('purchase/', views.purchasepage, name='purchasepage'),
  path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
  path('product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
  path('sales/<int:sale_id>/edit/', views.edit_sales, name='edit_sales'),
  path('sales/<int:sale_id>/delete/', views.delete_sale, name='delete_sale'),
  path('purchase/<int:purchase_id>/edit/', views.edit_purchase, name='edit_purchase'),
  path('purchase/<int:purchase_id>/delete/', views.delete_purchase, name='delete_purchase'),
  path('product/<int:product_id>/', views.singleproduct, name='singleproduct'),

]
