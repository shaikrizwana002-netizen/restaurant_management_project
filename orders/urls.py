from django.urls import path
from .views import UpdateOrderStatusView

urlpatterns = [
        path('update-order_status/', UpdateOrderStatusView.as_view(), name='update_order_status'),
]

{
    "id": 1,
    "status": "Completed"
}