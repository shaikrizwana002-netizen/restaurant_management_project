url.py
from django.urls import path
from .views import CreateUserReviewView, MenuItemReviewsView

urlpatterns = [
    path('reviews/create/', CreateUserReviewView.as_view(), name='create-review'),
    path('reviews/menu/<int:menu_item_id>/', MenuItemReviewsView.as_view(), name='menu-item-reviews'),
]
