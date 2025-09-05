< div class="datetime">
   <p>Current Date: {{ current-date }}</p>
   <p>Current Time: {{ current-tome/format-time }}</p>
   </div>

from django.shortcuts import render
from datetime import datetime
def home-view(request):
    now = datetime.now()
    context = {
        'current-date': now.date(),
        'current-time': now.time(),
        }
        return render(request, 'home.html', context)

from django import template

register = template.Library()

@register.filter
def format-time(value):
    return value.strftime('%I:%M %p')  #,10:35 AM
    {% load custom-filters %}

