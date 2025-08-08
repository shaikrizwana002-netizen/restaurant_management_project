# settings.py
RESTAURANT_NAME = "YUMMY CHEESE BITE"

# view.py
from django.conf import settings
from django.shortcuts import render

def homepage(request):
    context = {'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request, 'homepage.html', context)
    <!__ homepage.html __>
    <h1>Welcome to {{restaurant_name}}</h1>
    # models.py
    from django.db import models
    class Restaurant(models.Model):
        name = models.CharField(max_length=100)
        