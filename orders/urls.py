from django.urls import path
from .views import UpdateOrderStatusView
from .views import RestaurantInfoView

urlpatterns = [
        path('update-order_status/', UpdateOrderStatusView.as_view(), name='update_order_status'),
]

{
    "id": 1,
    "status": "Completed"
}


urlpatterns = [
    path('api/restaurant-info/', RestaurantInfoView.as_view(), name='restaurant-info'),
]
