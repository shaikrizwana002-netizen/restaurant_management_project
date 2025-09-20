#  models.py
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)


# views.py
from rest_framework import viewsets, filters
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name'] 

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter'],
}

{ 
  "count":2,
  "next": null,
  "previous": null,
  "results": [
    {
        "id": 1,
        "name": "Cheeseburger",
        "description": "Grilled beef paty with cheese",
        "price": "5.99",
        "is_available": true
    },
    ...
    ]
}