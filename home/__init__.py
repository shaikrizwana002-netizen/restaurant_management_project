from django.conf import settings
from django.shortcuts import render

def homepage(request):
    phone = settings.RESTAURANT_PHONE
    return render(request, 'homepage.html', {'phone': phone})

<div class="contact-section">
    <p class="phone-label"> call Us:</p>
    <p class ="phone-number">{{ phone }}</p>   
</div>