from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    def __str__(self):
        return  self.name

 from django.contrib import admin
 from django.urls import path,include
 from django.conf import settings
 from django.conf.urls.static import static       