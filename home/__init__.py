from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    def __str__(self):
       return self.name


<!DOCTYPE.html>
<html>
<head>
    <title>Restaurant Homepage/<title>
</head>
<body>
     <h1>Welcome to {{ restaurant.name }}</h1>
     <p> Call us at: <strong>{{ restaurant.phone_number }}</strong></p>
</body>
</html>    

