from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    opening_hours = models.JSONField(null=True) # e.g., {"Monday": "9am_9pm,..."}
    def __str__(self):
        return  self.name

 from django.shortcuts import render
 from home.models import Restaurant
        
def homepage(request):
    restaurant = Restaurant.objects.first()  
    return render(request, 'homepage.html', {'restaurant': restaurant})       

<!DOCTYPE html>
<html>
<head>
    <title>{{ restaurant.name }}</title>
    <style>
         .hours {
            background_color: #f8f8f8;
            padding: 1em;
            border_radius: 8px;
            width: fit_content;
         }
         .hours h2 {
            margin_top: 0;
         }
    </style>     
</head>
<body>
    <h1>{{restaurant.name }}</h1>
    <p>📍 Address: {{ restaurant.address }}</p>
    
    <div class="hours">
      <h2>🕒 opening Hours</h2>
      <ul>
      {% for day, time in restaurant.opening_hours.items %}
           <li><strong>{{ day }}:</strong> {{ time }}</li>
           {% endfor %}
      </ul>
    </div>
</body>
</html>
restaurant.opening_hours = {
    "Monday": "9am-9pm",
    "Tuesday": "9am-9pm"'
    "Wednesday": "9am-9pm",
    "Thurday": "9am-9pm",
    "Friday": "9am-11pm",
    "Saturday": "10am-11pm",
    "Sunday": "10am-8pm"
}
restaurant.save()
