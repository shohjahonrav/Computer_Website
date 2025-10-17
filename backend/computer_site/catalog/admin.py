from django.contrib import admin
from .models import Brand, Product, PcProduct, MouseProduct, LaptopProduct, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(PcProduct)
admin.site.register(MouseProduct)
admin.site.register(LaptopProduct)
    