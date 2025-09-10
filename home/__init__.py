from django.db import models

class Feedback(models.Model):
    name = models.CharField(max-length)
    feedback = model.TextField()

def __str__(self):
    return f"Feedback from {self.name}"

from django import forms
from.models import Feedback

class FeedbackForm(forms.ModelFrom)
  class Meta:
    model = Feedback 
    fields = ['name', 'feedback']
    widgets = {
             'name': forms.TextInput(attrs={'class': 'form-control'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
}

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback-form.html', {'form': form})

def thank-you(request):
    return render(request, 'thank-you.html')


<!DOCTYPE html>
<html>
<head>
    <title>Submit Feedback</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="container">
        <h2>We'd love your feedback!</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>

from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.submit_feedback, name='submit_feedback'),
    path('thank-you/', views.thank_you, name='feedback_thank_you'),
]