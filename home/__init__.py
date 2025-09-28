from django.db import models
from django.contrib.auth.models import user

class order(models.Model):
    status-CHOICES=[
        ('PENDING','PENDING'),
        ('Processing','processing'),
        ('cancelled','cancelled'),
        ('completed','completed'),
    ]

    user=models.foreignkey(User, on-delete=models.CASCADE)
    order-id = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    # other fields...

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import get_object_or_404

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['delete'], url_path='cancel')
    def cancel_order(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)

        # Ensure the user owns the order
        if order.user != request.user:
            return Response(
                {"error": "You are not authorized to cancel this order."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Update status
        order.status = 'Cancelled'
        order.save()

        return Response(
            {"message": f"Order {order.order_id} has been cancelled."},
            status=status.HTTP_200_OK
        )

from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'order_id', 'status', 'user']

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


Authorization: Token <your_token>