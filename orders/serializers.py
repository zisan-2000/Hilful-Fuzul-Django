from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all(), write_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_detail', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'name', 'email', 'phone_number', 'alt_phone_number',
            'country', 'district', 'area', 'address_details', 'total',
            'shipping_cost', 'grand_total', 'payment_method', 'order_items'
        ]
