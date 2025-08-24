from django.db import models
from django.contrib.auth.models import User
class MenuItems(models.Models):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def__str__(self):
        return self.name
        
class Order(models.Models):
    STATUS_CHOICES = [
        ('PENDING', 'pending'),
        ('CONFIRMED', 'confirmed'),
        ('DELIVERED', 'delivered'),
        ('CANCELED', 'canceled'),
    ]        
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_items = models.ManyToManyField(MenuItem, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return f"Order #{self.id} by {self.customer.username}"

