from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem
from .serializers import DailySpecialSerializer

class DailySpecialsView(APIView):
    def get(self, request):
        specials = MenuItem.objects.filter(is_daily_special=True)
        serializer = DailySpecialSerializer(specials, many=True)
        return Response(serializer.data)

class MenuItemIngredientsView(RetrieveAPIView):
    queryset = MenuItem.objects.all()

    def retrieve(self, request, *args, **kwargs):
        menu_item = self.get_object()
        ingredients = menu_item.ingredients.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)