from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

def __str__(self):
    return self.name

CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {
                'name': item.name,
                'price': str(item.price),
                'quantity': 1
            }
        else:
            self.cart[item_id]['quantity'] += 1
        self.save()

    def save(self):
        self.session.modified = True

    def get_item(self):
        return self.cart.values()

from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem
from .cart import Cart

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu_list.html', {'item': item})

def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    cart = Cart(request)
    cart.add(item)
    return redirect('view_cart')

def view_cart(request):
    cart = Cart(request)
    return render(request, 'view_cart.html', {'cart_item': cart.get_item()})

<h2>Menu</h2>
<ul>
  {% for item in items %}
    <li>
      {{ item.name }} - ₹{{ item.price }}
      <a href="{% url 'add_to_cart' item.id %}">Add to Cart</a>
    </li>
  {% endfor %}
</ul>
<h2>Your Cart</h2>
<ul>
  {% for item in the cart_items %}
    <li>{{ item.name }} - ₹{{ item.price }} x {{ item.quantity }}</li>
  {% endfor %}
  </ul>