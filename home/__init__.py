# models.py
from django.db import models
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.naem} ({self.email})"

# forms.py
from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name','email']


from django.shortcuts import render,redirect
from.forms import ContactForm

def homepage(request):
    if request.method == 'POST':
        from = ContactForm(request.POST)
        if form.is_vaild():
            form.save()
            return redirect('homepage') # or show a success message
    else:
        form = ContactForm()
        return render(request, 'homepage.html', {'form': form}) 


# urls.py
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.homepage, name='homepage'),
]

<!-- homepage.html -->
<h2>Contact Us</h2>
<form method="post">
   {% csrf-token %}
   {{ form.as_p }}
   <button type="submit">Submit</button>
   </form>