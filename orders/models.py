from django.db import models

class OrderManager(models.Manager):
    def with_status(self, status):
        return self.filter(status=status)

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    # Attach the custom manager
    objects = OrderManager()

    def __str__(self):
        return f"{self.customer_name} - {self.product_name} ({self.status})"