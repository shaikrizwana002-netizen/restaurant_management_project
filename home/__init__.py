from django.db import models

class TodaysSpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

from django.shortcuts import render
from .models import TodaysSpecial

def homepage_view(request):
    specials = TodaysSpecial.objects.all()
    return render(request, 'homepage.html', {'specials': specials})

<h2>Today's Specials</h2>
<ul>
  {% for item in specials %}
    <li>
      <strong>{{ item.name }}</strong><br>
      {{ item.description }}<br>
      ₹{{ item.price }}
    </li>
  {% empty %}
    <li>No specials available today.</li>
  {% endfor %}
</ul>

