from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    # Add this new field for opening days
    operating_days = models.CharField(
    max_length=50,
    help_text="Comma_Separated list of operating days, e.g., 'Mon, Tue, Wed, Thu, Fri'"
    )
    def __str__(self):
        return self.name

from restaurant.models import Restaurant
# Create a new restaurant instance
r = Restaurant(name="Spice Villa", address="123 Curry Lane", operating_days="Mon, Tue, Wed, Thu, Fri")        
r.save()

# Retrieve and check
restaurant = Restaurant.objects.get(name="Spice Villa)
print(restaurant.operating_days) # Mon, Tue,Wed, Thu, Fri