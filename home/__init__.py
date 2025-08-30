from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return  self.name

 from django.shortcuts import rend
 from .models import Restaurant
        
def homepage(request):
    restaurant = Restaurant.objectrestaurant = Restaurant.objects.first()  # or use get(id=1) if you have a specific one
    return render(request, 'homepage.html', {'restaurant': restaurant})       

    <h2>Visit Us</h2>
    <p>{{ restaurant.address }}</p>