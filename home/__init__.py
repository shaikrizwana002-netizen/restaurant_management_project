from django.db import models
from django.contrib.auth.models import User

class Userfile(models.Model):
    user = models.OneToOneField(User, on_delete=models. CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return self.name