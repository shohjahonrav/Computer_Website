from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()

  def __str__(self):
    return self.name
  


class Brand(models.Model):
  name = models.CharField(max_length=100, unique=True)
  logo = models.ImageField(upload_to='brands/', blank=True, null=True)

  def __str__(self):
    return self.name


class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
  brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='products')
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  base_price = models.DecimalField(max_digits=10, decimal_places=2)
  discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
  is_active = models.BooleanField(default=True)

  def discounted_price(self):
        return self.base_price - (self.base_price * self.discount_percent / 100)

  def __str__(self):
     return self.name

class PcProduct(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pc_details')
  ram = models.CharField(max_length=200)
  mother_board = models.CharField(max_length=200)
  gpu = models.CharField(max_length=200)
  power_block = models.CharField(max_length=200)
  cpu = models.CharField(max_length=200)
  ssd = models.CharField(max_length=200, blank=True, null=True)
  hdd = models.CharField(max_length=200, blank=True, null=True)
  adapters = models.CharField(max_length=250, blank=True, null=True)
  coolers = models.CharField(max_length=200)

  def __str__(self):
     return f"{self.product.name} - PC Specs"

class LaptopProduct(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='laptop_details')
  ram = models.CharField(max_length=200)
  mother_board = models.CharField(max_length=200)
  gpu = models.CharField(max_length=200)
  battery = models.CharField(max_length=200)
  cpu = models.CharField(max_length=200)
  ssd = models.CharField(max_length=200, blank=True, null=True)
  hdd = models.CharField(max_length=200, blank=True, null=True)
  weight = models.DecimalField(max_digits=6, decimal_places=2)
  charger = models.CharField(max_length=100)
  display = models.CharField(max_length=200)
  web_cam = models.CharField(max_length=200)
  color = models.CharField(max_length=100)
  

  def __str__(self):
     return f"{self.product.name} - Laptop Specs"

class MouseProduct(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mouse_details')
  dpi = models.IntegerField()
  color = models.CharField(max_length=50)
  is_wireless = models.BooleanField(default=False)

  def __str__(self):
     return f"{self.product.name} - Mouse Specs"

      