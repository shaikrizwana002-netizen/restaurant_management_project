from django.db import models
from account.models import Customer # assuming this is your user model
from home.models import Product # assuming this is your product model

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    customer = models.ForignKey(Customer, on_delete=models.CASCADE, related)
    order_items = models.ManyToManyField(Product, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order_id} by {self.customer}"

from rest_framework import serializers
from .models import Order
from home.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class m eta:
        model = Product
        fields = ['id', 'name', 'price' # adjust fields as needed
         
class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    order_items = ProductSerializer(many=True)

    class meta:
    model = Order
    fields = ['order)id', 'customer_name', 'order_items', 'total_price', 'created_at']
    
    
from rest_framework.generics import RetrieveAPIView
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_400

class OrderDetailView(RetrieveAPIView):
    serializer_class OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        order_id = self.kwargs.get('order_id')
        return get_object_or_400(Order, order_id=order_id)            


from django.urls import path
from .views import OrderDetailView

urlpatterns = [
    path('<str:order_id>/', OrderDetailView.as_view(), name='order-detail'),
]


curl -H "Authorization: Token your_token_here" http://localhost:8000/orders/ORD12345/
