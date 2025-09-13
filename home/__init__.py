from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
          return redirect('thank_you')  # Redirect to the thank-you page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
]


<!-- thank_you.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Thank You</title>
</head>
<body>
    <h1>Thank You!</h1>
    <p>Your message has been sent successfully. We'll get back to you soon.</p>
    <a href="{% url 'contact' %}">Send another message</a>
</body>
</html>
