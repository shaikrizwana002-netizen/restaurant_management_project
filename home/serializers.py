from rest_framework import serializers
from .models import MenuCategory
from .models import Restaurant

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'phone_number', 'opening_hours', 'description']
