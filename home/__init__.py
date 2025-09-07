 # views.py
 from django.shortcuts import render
 import random

 def order-confirmation(request):
    # Simulate an order number for demonstration
    order_number = random.randint(100000, 999999)
    return render(request, 'order_confirmation.html', {'order_number': order_number})

<!__ templates/order_confirmation __>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Order Confirmation</title>
</head>
<body>
    <h1> Order Confirmed!</h1>
    <p>Thank You for your purchase</h1>.
    <p><strong>Order Number:</strong>
</body>
</html>

 # urls.py
 from django.urls import path
 from . import views
 urlpatterns = [
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),

 ]