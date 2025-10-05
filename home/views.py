from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem
from .serializers import DailySpecialSerializer

class DailySpecialsView(APIView):
    def get(self, request):
        specials = MenuItem.objects.filter(is_daily_special=True)
        serializer = DailySpecialSerializer(specials, many=True)
        return Response(serializer.data)
