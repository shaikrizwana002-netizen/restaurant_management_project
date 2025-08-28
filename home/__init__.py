# models.py
from django.db import models

class   modelsenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def --str--(self):
        return self.name

# views.py
from django.shortcuts import render
from.models import modelsenuItem
def menu_page(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': items})

    #urls.py
    from django.urls import path
    from . import views          

    urlpatterns = [ 
        path('menu/', views.menu_page, name='menu'),
    ]

 <!-- templates/menu.html -->
 <!DOCTYPE html>
 <html>
 <head>
     <title>Menu</title>
</head>
<body>   
    <h1>Our Menu</h1>
    <ul>
    {% for item in menu_items %}
       <li>
          <strong>{{item.name }}</strong> - ₹{{ item.price }}<br>
          <em>{{ item.description }}</em>
       </li>
    {% empty %}
       <li>No items available.</li>
       {% render %}
  </ul>
</body>
</html>      