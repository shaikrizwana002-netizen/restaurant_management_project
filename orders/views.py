from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from .models import Order
from .serializers import OrderStatusUpdateSerializer
from .models import Restaurant
from .serializers import RestaurantSerializer
from .serializer import MenuCategorySerializer

class UpdateOrderStatusView(APIView):
    def post(self, request):
        order_id = request.data.get('id')
        new_status = request.data.get('status')
       
       try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=http_status.HTTP_404_NOT_FOUND)

        serializer = OrderStatusUpdateSerializer(order, data={'status': new_status}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"Order #{order.id} status updated to '{order.status}'."}, status=http_status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)

class RestaurantInfoView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

