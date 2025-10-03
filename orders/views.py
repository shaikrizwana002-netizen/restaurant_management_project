from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response({'error': 'Coupon code is required.'}, status=status.HTTP_400_BAD_REQUEST)

        today = timezone.now().date()
        try:
            coupon = Coupon.objects.get(code=code, is_active=True)
            if coupon.valid_from <= today <= coupon.valid_until:
                return Response({
                    'success': True,
                    'discount_percentage': float(coupon.discount_percentage)
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Coupon is not valid today.'}, status=status.HTTP_400_BAD_REQUEST)
        except Coupon.DoesNotExist:
                return Response({'error': 'Invalid or inactive coupon code.'}, status=status.HTTP_400_BAD_REQUEST)
