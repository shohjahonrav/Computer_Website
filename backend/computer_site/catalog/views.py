from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, PcProduct, LaptopProduct, MouseProduct, Brand, Category
from .serializers import ProductSerializer, PcProductSerializer, LaptopProductSerializer, MouseProductSerializer, BrandSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class BrandViewSet(viewsets.ModelViewSet):
  queryset = Brand.objects.all()
  serializer_class = BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class PcProductViewSet(viewsets.ModelViewSet):
  queryset = PcProduct.objects.select_related('product').all()
  serializer_class = PcProductSerializer

class LaptopProductViewSet(viewsets.ModelViewSet):
  queryset = LaptopProduct.objects.select_related('product').all()
  serializer_class = LaptopProductSerializer

class MouseProductViewSet(viewsets.ModelViewSet):
  queryset = MouseProduct.objects.select_related('product').all()
  serializer_class = MouseProductSerializer
