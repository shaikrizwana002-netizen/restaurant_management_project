from django.shortcuts import render

def menu_view(request):
    menu_items = [
        {'name': 'Marherita Pizza', 'price': '₹250'},
        {'name': 'Paneer Tikka', 'price': '₹160'},
        {'name': 'Masala Dosa', 'price': '₹120'},
        {'name': 'Gulab Jamun', 'price': '₹80'},
    ]
    return render(request, 'menu.html', {'menu_items':menu_items})
    <!DOCTYPE html>
    <html>
    <head>
    <title>Menu</title>
    <style>
    body { font_family: Arial, sans_serif; padding: 20px; }
    h1 { color: #333;}
    ul {list_style: none; padding:0;}
    li { margin: 10px 0; padding: 10px; background: #f9f9f; border_radius: 5px; }
    </style>
    </head>
    <body>
    <h1>Perpex Bistro Menu</h1>
    <ul>
    {% for item in menu_items %}
    <li><strong>{{ item.name}}</strng> _ {{ item.price}}</li>

    from django.urls import path
    from. views import menu_view

    urlpatterns = [
        path('menu/', menu_view, name='menu'),
    ]

    menu_items = MenuItem.objects.all()