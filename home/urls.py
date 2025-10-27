from django.urls import path
from .views import CreateUserReviewView

urlpatterns = [
        path('reviews/create/', CreateReviewView.as_view(), name='create-review'),
]