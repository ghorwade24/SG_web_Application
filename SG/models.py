from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending") 
    
    def __str__(self) -> str:
        return f"Order {self.id} - {self.user if self.user else 'Guest'}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey('MenuCard', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"
class EnquriForFranchasi(models.Model):
    
    Invester_name = models.TextField(max_length=50)
    Phone_number = models.IntegerField()
    Email = models.EmailField( max_length=254)
    City = models.TextField(max_length=240)
    Locations_are_you_oppening = models.TextField(max_length=400)
    
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.Invester_name}"
    

from django.db import models

class MenuCard(models.Model):
    # Define the available dishes as choices
    DISHES = [
        ('Pani Puri', 'Pani Puri'),
        ('Masala Puri', 'Masala Puri'),
        ('Ragada Puri', 'Ragada Puri'),
        ('Dahi Puri', 'Dahi Puri'),
        ('Shev Puri', 'Shev Puri'),
        ('SPDP', 'SPDP'),
        ('Sukhi Bhel', 'Sukhi Bhel'),
        ('Aoli Bhel', 'Aoli Bhel'),
        ('Farasan Bhel', 'Farasan Bhel'),
    ]

    # The dish name, selected from the predefined list
    dish_name = models.CharField(max_length=50, choices=DISHES)
    
    
    # Price of the dish
    price = models.DecimalField(max_digits=6, decimal_places=2)  # e.g. 9999.99 max price
    
    # Optional field for adding description
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='dish_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.dish_name} - Rs {self.price}'
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    feedback = models.TextField()
    
    # This is optional but helpful for displaying in the admin interface
    def __str__(self):
        return self.name


    
    
    
