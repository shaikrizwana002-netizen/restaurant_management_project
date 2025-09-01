from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return  self.name

 from django.shortcuts import render
 from .models import Restaurant
        
def homepage(request):
    restaurant = Restaurant.object.restaurant = Restaurant.objects.first()  #  Assuming one restaurant
    return render(request, 'homepage.html', {'restaurant': restaurant})       

<!DOCTYPE html>
<html>
<head>
    <title>Welcome to our Restaurant>
</head>
<body>
    <h1>{{restaurant.name }}</h1>
    <p>📍 Address: {{ restaurant.address }}</p>
</body>
</html> 