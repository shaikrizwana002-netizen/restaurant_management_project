from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now=True)
    status = models.ForeignKey('orders.OrderStatus', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
