from django.urls import path
from .views import UpdateOrderStatusView
from .views import RestaurantInfoView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryViewSet

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

router = DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename='menu-category')

urlpatterns = [
    path('api/', include(router.urls)),
]