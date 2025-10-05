from django.urls import path
from .views import UpdateOrderStatusView

urlpatterns = [
        path('update-status/', UpdateOrderStatusView.as_view(), name='update_order_status'),
]

{
    "order_id":1,
    "status": "Delivered"
}