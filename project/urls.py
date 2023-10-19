from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop.views import CategoryViewset
from shop.views import ProductViewset
from shop.views import ArticleViewset

# from shop.views import CategoryAPIView
# from shop.views import ProductAPIView

router = routers.SimpleRouter()

router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
    # path('api/category/', CategoryAPIView.as_view()),
    # path('api/product/', ProductAPIView.as_view())
]
