from rest_framework import serializers
from .models import Product, Category
from writers.models import Writer
from publishers.models import Publisher
from writers.serializers import WriterSerializer
from publishers.serializers import PublisherSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    writer = WriterSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    # ✅ Correct queryset for ForeignKey fields
    writer_id = serializers.PrimaryKeyRelatedField(
        queryset=Writer.objects.all(), source='writer', write_only=True
    )
    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), source='publisher', write_only=True
    )
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'original_price', 'discount',
            'stock', 'available', 'image', 'pdf',
            'writer', 'publisher', 'category',
            'writer_id', 'publisher_id', 'category_id'
        ]
