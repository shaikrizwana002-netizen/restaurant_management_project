from django.db import models

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"


from rest_framework import serializers
from .models import ContactFormSubmission

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = ['id', 'name', 'email', 'message']


from rest_framework.generics import CreateAPIView
from rest_framework.response import Response 
from rest_framework import status
from .models import ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer

class ContactFormSubmissionView(CreateAPIView):
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Contact form submitted successfully."},
                status= status.HTTP_201_CREATED
            )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.urls import path
from .view import ContactFormSubmissionView

urlpatterns = [
    path('api/contact/', ContactFormSubmissionView.as_view(), name='contact_form_submit'),
]

from django.urls import path, include

urlspatterns = [
    path('', include('home.urls')),
    # other routes...
]

