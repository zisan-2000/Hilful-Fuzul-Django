from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email', 'phone_number',
        'total', 'shipping_cost', 'grand_total',
        'payment_method'
    )
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('payment_method', 'country', 'district')
    readonly_fields = ('total', 'shipping_cost', 'grand_total')
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__name', 'product__name')
