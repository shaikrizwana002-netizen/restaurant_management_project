# menu/views.py
from rest_framework.views import
from rest_framework.response import

class MenuView(APIView):
    def get(self, request):
        menu = [
            {
                "name": "Margherita pizza", 
                "description": "Classical pizza with tomato sauce, mozzarella, and basil.",
                "price": "8.99"
                },
                {
                "name": "Caesar Salad",
                "description": "Romaine lettuce eith Ceasar dressing, croutons, and parmesan.",
                "price": 6.50
                },
                {
                "name": "Spaghetti Carbonara",
                "description": "Pasta with eggs, cheese, pancetta, and pepper",
                "price": 10.75
            }
        ]     
        return Response(menu)
