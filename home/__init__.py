# models.py
from django.db import models

class   modelsenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def__str__(self):
        return self.name

python manage.py makemigrations

python manage.py migrate

from django.contrib import admin
from.models import MenuItem

admin.site.register(MenuItem)