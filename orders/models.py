from django.db import models
from products.models import Product

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    alt_phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    address_details = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, related_name='orders', through='OrderItem')

    def __str__(self):
        return f"Order {self.id} by {self.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity} for {self.order}"
