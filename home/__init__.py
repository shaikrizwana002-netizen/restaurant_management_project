from django.db import models
from home.models import MenuItem
from decimal import Decimal

class Order(models.Model):
    order_id = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order {self.order_id}"

    def calculate_total(self):
        total = Decimal('0.00')
        for item in self.items.all():
            total += item.price * item.quantity
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

        
from django.test import TestCase
from home.models import MenuItem
from orders.models import Order, OrderItem
from decimal import Decimal

class OrderTotalTestCase(TestCase):
    def setUp(self):
        self.item1 = MenuItem.objects.create(name="Burger", price=Decimal('5.00'))
        self.item2 = MenuItem.objects.create(name="Fries", price=Decimal('2.50'))
        self.order = Order.objects.create(order_id="ORD123")

        OrderItem.objects.create(order=self.order, menu_item=self.item1, quantity=2, price=self.item1.price)
        OrderItem.objects.create(order=self.order, menu_item=self.item2, quantity=3, price=self.item2.price)

    def test_calculate_total(self):
        expected_total = Decimal('5.00') * 2 + Decimal('2.50') * 3
        self.assertEqual(self.order.calculate_total(), expected_total)
