# home/serializers.py
from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers):
class Meta:
    model = MenuCategory
    fields = ['name']

# home/views.py
from rest_framework.generics import ListAPIView
from .models import MenuCategory    
from .serializers import MenuCategorySerializer

class MenuCategoryListView(ListAPIView):
queryset = MenuCategory.objects.all()
serializer_class = MenuCategorySerializer

# home/urls.py
from django.urls import path
from .views import MenuCategoryListView

urlpatterns = [
    path('menu_categories/', MenuCategoryListView.as_view(), name='menu_category_List'),
]