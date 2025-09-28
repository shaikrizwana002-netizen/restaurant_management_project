# orders/utils.py

import string
import secrets
from .models import Order  # Adjust if your model is named differently

def generate_unique_order_id(length=8):
    """
    Generates a unique alphanumeric ID for an order.
    
    Args:
        length (int): Length of the ID string.
    
    Returns:
        str: A unique alphanumeric ID.
    """
    characters = string.ascii_uppercase + string.digits

    while True:
        order_id = ''.join(secrets.choice(characters) for _ in range(length))
        if not Order.objects.filter(order_id=order_id).exists():
            return order_id

# orders/models.py

from django.db import models
from .utils import generate_unique_order_id

class Order(models.Model):
    order_id = models.CharField(max_length=10, unique=True, blank=True)
    # other fields...

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_unique_order_id()
        super().save(*args, **kwargs)