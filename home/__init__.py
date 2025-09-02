from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    def __str__(self):
       return self.name


<!DOCTYPE.html>
<html>
<head>
    <title>{{ restaurant.name }}</title>
</head>
<body>
     <h1>Welcome to {{ restaurant.name }}</h1>
     {% if restaurant.logo %}
        <img src="{{ restaurant.logo.url }}" alt="{{ restaurant.name }}" Logo style="max_width:200px;">
    {% ielse %}
         <p>No logo available.</p>
    {% endif %}
</body>
</html>    

