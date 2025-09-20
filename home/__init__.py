# models.py
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

        
# serializers.py
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0.0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value
        
# views.py
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can update

    def update(self, request, pk=None):
        try:
            item = self.get_object()
            serializer = self.get_serializer(item, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('api/', include(router.urls)),
]onse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)