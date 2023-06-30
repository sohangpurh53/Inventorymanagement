from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale, Product, Stock, Purchase
from .forms import SaleForm, ProductForm, PurchaseForm
from django.contrib import messages
# Create your views here.

def Homepage(request):
    purchases = Purchase.objects.all()
      
    products = Product.objects.all()

    sales = Sale.objects.all()

    for purchase in purchases:
        purchase.total = purchase.price*purchase.quantity

 
    
        


    for sale in sales:
        sale.total = sale.price*sale.quantity

    stocks = Stock.objects.all()



    return render(request, 'homepage.html', {'product':products, 'sales':sales, 'stocks':stocks, 'purchases':purchases } )

def productpage(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('Product Added Successfull'))
            return redirect('productpage')  # Redirect to a page showing the list of products
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form': form})


def salespage(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salespage')  # Redirect to a page showing the list of products
    else:
        form = SaleForm()
    return render(request, 'sale.html', {'form': form})

def purchasepage(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Purchase Product Added Successfull'))
            return redirect('purchasepage')  # Redirect to a page showing the list of products
    else:
        form = PurchaseForm()
    return render(request, 'purchase.html', {'form': form})

#product edit delete and single product
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, ('Product Delete Successfull'))
    return redirect('Homepage')

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

def singleproduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'singleproduct.html', context)

#sales delete and edit
def edit_sales(request, sale_id):
    sales = get_object_or_404(Sale, id=sale_id)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sales)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
    else:
        form = SaleForm(instance=sales)
    return render(request, 'edit_sales.html', {'form': form})

def delete_sale(request,  sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    stock = Stock.objects.get(product=sale.product)
    stock.increase_quantity(sale.quantity)
    sale.delete()
    messages.success(request, 'Sale deleted successfully')
    return redirect('Homepage')

#purchase edit and delete
def edit_purchase(request, purchase_id):
    purchases = get_object_or_404(Purchase, id=purchase_id)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchases)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
    else:
        form = PurchaseForm(instance=purchases)
    return render(request, 'edit_purchase.html', {'form': form})

def delete_purchase(request,  purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    stock = Stock.objects.get(product=purchase.product)
    stock.decrease_quantity(purchase.quantity)
    purchase.delete()
    messages.success(request, 'Purchase deleted successfully')
    return redirect('Homepage')
