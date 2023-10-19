from rest_framework.serializers import ModelSerializer

from shop.models import Category
from shop.models import Product

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'category']