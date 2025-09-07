<!-- templates/home.html -->
<a href="{% url 'place_order' %}" class="order-button">Order Now</a>

.order-button {
    display: inline-block;
    padding: 12px 24px;
    background-color: #28a745;
    color: white;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: background-color 0.3s ease;
}

.order-button:hover {
    background-color: #218838;ass="order-button">Order Now</a>
}

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('place-order/', views.place_order, name='place_order'),
]


 views.py
from django.shortcuts import render

def place_order(request):
    return render(request, 'place_order.html')

<!-- templates/place_order.html -->
<h1>Place Your Order</h1>
<p>This page will allow users to place their orders. Coming soon!</p>

