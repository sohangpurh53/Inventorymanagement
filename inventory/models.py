from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image', default=False)
   

    def __str__(self):
        return self.name


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=False)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        stock, created = Stock.objects.get_or_create(product=self.product)
        stock.increase_quantity(self.quantity)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(default=False, max_digits=10, decimal_places=2)
    sale_date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        stock = Stock.objects.get(product=self.product)
        stock.decrease_quantity(self.quantity)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    def increase_quantity(self, quantity):
        self.quantity += quantity
        self.save()

    def decrease_quantity(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            self.save()
        else:
            raise ValueError("Insufficient quantity")
