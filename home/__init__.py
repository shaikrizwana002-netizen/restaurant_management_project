from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return  self.name

 from django.shortcuts import render
 from home.models import MenuItem
        
def homepage(request):
    restaurant = MenuItem.objects.first()  
    return render(request, 'homepage.html', {'menu_items': menu_items})       

<!DOCTYPE html>
<html>
<head>
    <title>Menu</title>            border: 1px solid #ddd;

    <style>
         .menu_items {
            border: 1px solid #ddd;
            padding: 1em;
            margin_bottom: 1em;
            display: flex;
            align_items: center;
            }
            .menu_items img {
                max_width: 150px;
                margin_right:1em;
                border_radius: 8px;
            }
    </style>
</head>
<body>
     <h2>🍽️ Our Menu</h1>
    {% for item in menu_items %}
        <div class="menu-item">
            {% if item.image %}
                <img src="{{ item.image.url }}" alt="{{ item.name }}">
            {% endif %}
            <div>
                <h2>{{ item.name }}</h2>
                <p>{{ item.description }}</p>
                <p><strong>₹{{ item.price }}</strong></p>
            </div>
        </div>
    {% endfor %}
</body>
</html>    