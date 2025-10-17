from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, PcProductViewSet, LaptopProductViewSet, MouseProductViewSet, BrandViewSet, CategoryViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('pcs', PcProductViewSet)
router.register('laptops', LaptopProductViewSet)
router.register('mice', MouseProductViewSet)
router.register('brand', BrandViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

