from django.db import models
from django.utils import timezone
from datetime import timedelta

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_featured = models.BooleanField(default=False)  # ✅ New field

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    
    class DailySpecial(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        price = models.DecimalField(max_digits=6, decimal_places=2)
        available = models.BooleanField(default=True)
    
        @staticmethod
        def get_random_special():
            special = DailySpecial.objects.filter(available=True).order_by('?').first()
            return special  # Returns None if no specials are available
    
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    opening_hours = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.customer_name} ({self.start_time} - {self.end_time})"
