from django.urls import path
from .views import AvailableTablesAPIView

urlpatterns = [
    path('api/tables/available/', AvailableTablesAPIView(), name='available_tables_api'),
    ]