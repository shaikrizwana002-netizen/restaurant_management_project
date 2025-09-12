from django.db import models

class OpeningHour(models.Model):
    day = models.CharField(max_length=10) # e.g., Monday, Tuesday
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.day}: {self.open_time} - {self.close_time}"

from django.contrib import admin
from .models import OpeningHour 
admin.site.register(OpeningHour)

from django.shortcuts import render
from.models import OpeningHour
def homepage(request):
    hours = OpeningHour.objects.all().order_by('id') #  or order by day
    return render(request, 'homepage.html', {'opening_hours':hours})

<h2>Opening_Hours</h2>
<ul>
  {% for hour in opening_hours %}
    <li>{{ hour.day }}: {{ hour.open_time|time:"H:i" }} - {{ hour.close_time|time:"H:i" }}</li>
  {% endfor %}
</ul>

