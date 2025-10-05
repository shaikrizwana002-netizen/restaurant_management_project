from django.urls import path
from .views import DailySpecialsView

urlpatterns = [
    path('daily-specials/', DailySpecialsView.as_view(), name='daily-specials'),
]
