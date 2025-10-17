from rest_framework import serializers
from .models import PcProduct, LaptopProduct, MouseProduct, Product, Brand, Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Brand
    fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'


class PcProductSerializer(serializers.ModelSerializer):
  product = ProductSerializer()
    
  class Meta:
    model = PcProduct
    fields = '__all__'

  def create(self, validated_data):
    product_data = validated_data.pop('product')
    product = Product.objects.create(**product_data)
    pc_product = PcProduct.objects.create(product=product, **validated_data)
    return pc_product


class LaptopProductSerializer(serializers.ModelSerializer):
  product = ProductSerializer()
    
  class Meta:
    model = LaptopProduct
    fields = '__all__'


  def create(self, validated_data):
    product_data = validated_data.pop('product')
    product = Product.objects.create(**product_data)
    laptop_product = LaptopProduct.objects.create(product=product, **validated_data)
    return laptop_product

  
class MouseProductSerializer(serializers.ModelSerializer):
  product = ProductSerializer()

  class Meta:
    model = MouseProduct
    fields = '__all__'

  def create(self, validated_data):
    product_data = validated_data.pop('product')
    product = Product.objects.create(**product_data)
    mouse_product = MouseProduct.objects.create(product=product, **validated_data)
    return mouse_product    