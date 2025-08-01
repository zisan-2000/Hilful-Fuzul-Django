from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'writer', 'publisher', 'category',
        'price', 'original_price', 'discount', 'stock', 'available'
    )
    search_fields = ('name', 'writer__name', 'publisher__name')
    list_filter = ('available', 'category', 'publisher')
    list_editable = ('available', 'price', 'discount', 'stock')
