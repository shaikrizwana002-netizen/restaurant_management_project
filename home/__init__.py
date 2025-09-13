from django.db import models

class RestaurantInfo(models.Model):
  name = models.CharField(max_length=100)
  address = models.TextField()

def __str__(self):
    return self.name

from django.shortcuts import render
from .forms import ContactForm
from .models import RestaurantInfo

def contact_view(request):
        form = ContactForm()
        restaurant = RestaurantInfo.objects.first()  
        
    if request.method =='POST':
        form = ContactForm(request.POST)
         if form.is_valid():
            # Process form data
            return redirect('thank_you')

    return render(request, 'contact.html', {
        'form': form,
        'restaurant': restaurant
    })

<h2>Contact Us</h2>
<p><strong>Address:</strong> {{ restaurant.address }}</p>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
</form>
