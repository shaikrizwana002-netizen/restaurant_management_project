# settings.py
R ESTAURANT_ADDRESS = "123 Main Street, Eluru, Andhra Pradesh, India"

# models.py
class RestaurantInfo(models.Models):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

# views.py
from django.conf import settings
settingsfrom django.shortcuts import render    

def homepage(request):
    address = settings.RESTAURANT_ADDRESS
    return render(request, 'homepage.html', {'restaurant_address': address})


<!--homepage.html -->
<h2>Visit Us</h2>
<p>{{ restaurant_address }}</p>

<!-- Embedded Google Map -->
<iframe
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3876.123456789!2d81.123456!3d16.710123!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a123456789abcdef%3A0xabcdef123456789!2s123%20Main%20Street%2C%20Eluru%2C%20Andhra%20Pradesh!5e0!3m2!1sen!2sin!4v1691234567890"
  width="600"
  height="450"
  style="border:0;"
  allowfullscreen=""
  loading="lazy"
  referrerpolicy="no-referrer-when-downgrade">
  </iframe>
