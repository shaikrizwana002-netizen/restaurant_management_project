from django.db import models
from .utils import calculate_discount  # Adjust import path as needed

class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        total = 0
        for item in self.items.all():  # Assuming related_name='items' in OrderItem
            discounted_price = calculate_discount(item.product.price, item.quantity)
            total += discounted_price
        return total

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"