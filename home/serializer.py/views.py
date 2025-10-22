views.py
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import UserReview
from .serializers import UserReviewSerializer
from rest_framework.permissions import IsAuthenticated

class CreateUserReviewView(CreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
