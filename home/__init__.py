from django.contrib.auth.models import User
from rest_framework import serializers

class UserProfileSerializer(serializer.ModelSerializer):
     class Meta:
        model = UserProfileSerializer
        fields = ['first_name','last_name', 'email'] # Add other editable fields if needed

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from.serializer import UserProfileSerializer

class UserProfileViewSet(viewsets.Viewsets):
   permission_classes = [permission.IsAuthenticated]

   def update(self, requet):
       serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.urls import path
from.views import UserProfileViewSet

user_profile_view = UserProfileViewSet.as_view({'put': 'update'})

urlspatterns = [
    path('profile/update/', user_profile_view, name='profile-update')
]

{ "first_name": "Shaik",
"last_name": "Rizwana",
"email": "rizwana@example.com",
}