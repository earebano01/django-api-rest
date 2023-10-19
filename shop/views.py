from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


from shop.models import Category
from shop.serializers import CategorySerializer
from shop.models import Product
from shop.serializers import ProductSerializer

class CategoryViewset(ReadOnlyModelViewSet):
 
    serializer_class = CategorySerializer
 
    def get_queryset(self):
        return Category.objects.filter(active=True)

# class CategoryAPIView(APIView):

#     def get(self, *args, **kwargs):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
    
class CategorySerializer(ModelSerializer):
 
    class Meta:
        model = Category
        fields = ['id', 'name']

# class ProductAPIView(APIView):

#     def get(self, *args, **kwargs):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

class ProductViewset(ReadOnlyModelViewSet):
 
    serializer_class = ProductSerializer
 
    def get_queryset(self):
        return Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    
class ProductSerializer(ModelSerializer):
 
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'active']