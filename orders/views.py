from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from .models import Order

class UpdateOrderStatusView(APIView):
    def post(self, request):
        order_id = request.data.get('order_id')
        new_status = request.data.get('status')

        # Validate status
        valid_statuses = dict(Order.STATUS_CHOICES).keys()
        if new_status not in valid_statuses:
            return Response(
                {"error": "Invalid status value."},
                status=http_status.HTTP_400_BAD_REQUEST
            )

        # Validate order ID
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found."},
                status=http_status.HTTP_404_NOT_FOUND
            )

        # Update status
        order.status = new_status
        order.save()

        return Response(
            {"message": f"Order #{order.id} status updated to '{order.status}'."},
            status=http_status.HTTP_200_OK
        )
