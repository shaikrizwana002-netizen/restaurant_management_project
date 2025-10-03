from django.urls import path
from .views import TableDetailAPIView

urlpatterns = [
    path('api/tables/<int:pk>/', TableDetailAPIView.as_view(), name='table_detail_api'),
]


http://127.0.01:8000/api/tables/1/