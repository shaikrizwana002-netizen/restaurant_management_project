class Category(models.Model):
    Category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class MenuField(modles.Model):
    name = models.ChatrField(max_length=100)
    description = models.TextFDield()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category_name = models.ForeignKey(Category, =models.CASCADE)

    def __str__(self):
        return self.name        

from rest_framwork import serializers
from .models import MenuItem

class MenuItemSerializer(serializer.ModelSerializer):
class Meta:
    model = MenuItem
    fields = '__all__'

from rest_framwork.views import APIView
from.rest_framwork.response import Response
from rest_framwork import status
from .models import MenuItem
from .serializers import MenuItemSerializer

class FilteredMenuItemsView(APIView):
    def get(self, request):
        category_name = request.query_params.get('category')
        if category_name:
            items = MenuItem.objects.filter(category__category_name__iexact=category_name)
            serializer = MenuItemSerializer(items, many=True)
        else:
            items = MenuItem.objects.all()
            serializer = MenuItemSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)    

from django.urls import path
from .views import FilteredMenuItemsView

urlpatterns = [path('menu_items/', FilteredMenuItemsView.as_view(), name='filtered_menu_items'),]