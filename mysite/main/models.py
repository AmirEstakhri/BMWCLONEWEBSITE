from django.db import models
from django.core.validators import  MinLengthValidator ,MaxValueValidator , MinValueValidator
# Create your models here.


class BlogPost (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publishDate = models.DateField(auto_now_add=True)
    
    def __str__(self):
        
        return  self.title
    
from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField( blank=True,)
    star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    id = models.AutoField(primary_key=True) # primary key id  

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') 
    #<!-- id nemigire!     {% url 'product'product.id %}     -->
    is_sales = models.BooleanField(default=False) #takhfif  - (discounted)
    sales_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True) # (discounted) price
     
    def __str__(self):
        return self.name

# Customer Model
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')  
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')  #
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order {self.id} by {self.customer.email}"

from django.db import models

class SocialMedia(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
