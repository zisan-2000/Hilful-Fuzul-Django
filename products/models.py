from django.db import models
from writers.models import Writer
from publishers.models import Publisher

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    writer = models.ForeignKey(Writer, related_name='products', on_delete=models.SET_DEFAULT, default=1)
    publisher = models.ForeignKey(Publisher, related_name='products', on_delete=models.SET_DEFAULT, default=1)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    pdf = models.FileField(upload_to='products/pdfs/', null=True, blank=True)

    def __str__(self):
        return self.name
