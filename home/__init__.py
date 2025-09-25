from django.db import models

class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending', 'processing'])

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),       
        ('processing', 'Processing'),
    ]
    status + models.CharField(max_length=20, chocied=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ActiveOrderManager()

from orders.models import Order
active_orders = Order.objects.get_active_orders = Orders.objects.get_active_orders()
print(active_orders)    