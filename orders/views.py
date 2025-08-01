from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order, OrderItem
from products.models import Product
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('products').all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        products_data = data.pop('products', [])
        order_serializer = self.get_serializer(data=data)
        order_serializer.is_valid(raise_exception=True)
        order = order_serializer.save()

        for item in products_data:
            product_id = item.get('product_id')
            quantity = item.get('quantity', 1)

            try:
                product = Product.objects.get(id=product_id)
                price = product.price * quantity
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=price
                )
            except Product.DoesNotExist:
                order.delete()  # Order rollback
                return Response(
                    {"error": f"Product with id {product_id} does not exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        return Response(self.get_serializer(order).data, status=status.HTTP_201_CREATED)
