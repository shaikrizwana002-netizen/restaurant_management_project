# settings.py
RESTAURANT_NAME = "Yummy Restauarnt"

# views.py
from django.conf import settings
from.django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html', {
        'restaurant_name': settings.RESTAURANT_NAME
    })

    <!-- homepage.html -->
    <h1>Welcome to {{ restaurant_name }}</h1>