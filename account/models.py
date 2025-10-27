from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
