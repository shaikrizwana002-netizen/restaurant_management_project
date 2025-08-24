<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF_8">
   <title>Restaurant Menu</title>
   <style>
       body { font_family: Arial, san_serief; padding: 20px; background: #f9f9f9; }
       h1 { color: #333; }
       .menu_item { background: #fff; padding: 15px; margin_bottom: 10px; border_radius: 5px; box_shadow: 0 2px 5px rgba(0, 0, 0, 0.1); }
       .menu_item h2 { margin: 0; font_size: 1.2em;}
       .menu_item p { margin: 5px 0; color: #666; }
       .price { font_weight: bold; color: #2c3e50; }
    </style>
</head>
<body>
    <h1>Our Menu</h1>
    {% for item in menu_items %}
    <div class="menu_items">
       <h2>{{ item.name }}</h2>
       <p>{{ item.description }}</p>
       <p class="price">₹{{ item.price }}</p>
    </div>
   {% empty %} 
   <p>No menu items available at the moment.</p>
   {% endfor %}
</body>
</html>   