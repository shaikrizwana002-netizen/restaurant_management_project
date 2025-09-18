from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    #Add your existing fields here, for example:
    customer_name = models,CharField(max_length=100)
    order_data = models.DataTimeField(auto_now)

    #New field to track status
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
