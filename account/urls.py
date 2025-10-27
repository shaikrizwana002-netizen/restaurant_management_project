from django.urls import path
from .views import UpdateAvailabilityView

urlpatterns = [
    path('menu-items/<int:pk>/availability/', UpdateAvailabilityView.as_view(), name='update-availability'),
]
