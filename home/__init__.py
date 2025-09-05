< !__ templates/faq.html __>
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>FAQs</title>
   <style>
   body { font-family: Arial, sans-serif; padding: 20px; }
   h1 { colo: #333; }
   .faq-t-item { margin-bottom: 20px; }
   .question { font-weight: bold; }
   .answer { margin-left: 10px; }
   </style>
</head>
<body>
  <h1>Frequently Asked Question</h1>
  <div class="faq-item">
  <div= class="question">Q: How do I reset my password?</div>
  <div clas="answer">A: Click on "Forget Password" at login and follow the instruction.</div>
  </div>
<div class="faq-item">
  <div class="question">   Q: Can I edit my submission after uploading?</div>
  <div class="answer">A: Yes, you can edit it until the .</div>
  </div>
</body>
</html>  

from django.shortcuts import render

def faq-view(request):
    return render(request, 'faq.html')

from django.urls import path
from.views import faq-view

from django.urls import path
from .views import faq-view
urlpatterns =[
    path('faq/', faq-view, name='faq'),
]

<a href="{%  url 'faq' %}">FAQs</a>

<a href="/faq/">FAQs</a>