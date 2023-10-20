from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from shop.models import Category
from shop.models import Product
from shop.models import Article

class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category']



class CategorySerializer(ModelSerializer):

    # products = ProductSerializer(many=True)
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']

    def get_products(self, instance):
            queryset = instance.products.filter(active=True)
            serializer = ProductSerializer(queryset, many=True)
            return serializer.data