from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from shop.models import Category
from shop.models import Product
from shop.models import Article

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category', 'ecoscore']


class ProductDetailSerializer(serializers.ModelSerializer):

    article = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category', 'article']

    def get_article(self, instance):
         queryset = instance.articles.filter(active=True)
         serializer = ArticleSerializer(queryset, many=True)
         return serializer.data
    

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
          model = Category
          fields = ['id', 'date_created', 'date_updated', 'name', 'description']
    
    def validate_name(self, value):
          if Category.objects.filter(name=value).exists():
               raise serializers.ValidationError('Category already exists')
          return value
     
    def validate(self, data):
          if data['name'] not in data['description']:
               raise serializers.ValidationError('Name must be in description')
          return data


class CategorySerializer(ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']

    def get_products(self, instance):
            queryset = instance.products.filter(active=True)
            serializer = ProductSerializer(queryset, many=True)
            return serializer.data
    

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']
    
    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data