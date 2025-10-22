# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)



class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class UserReview(models.Model):
    """
    Model to store user ratings and comments for specific menu items.
    """
    # 1. Foreign Key to the User who left the review (required)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

    # 1. Foreign Key to the Menu Item being reviewed (required)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='reviews')

    # 1. Integer field for the rating, constrained between 1 and 5 (required)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating must be between 1 and 5."
    )

    # 1. Text field for the comment (required)
    comment = models.TextField(blank=True, null=True)

    # 3. Optional field to record the creation date
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a user can only review a single menu item once
        unique_together = ('user', 'menu_item')
        # Custom ordering for displaying reviews
        ordering = ['-review_date']

    def __str__(self):
        return f'{self.user.username} rated {self.menu_item.name} ({self.rating}/5)'

    # You could add a property to check if the review is positive/negative:
    @property
    def is_positive(self):
        return self.rating >= 4
