from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView
from .models import Table
from .serializers import TableSerializer

class TableDetailAPIView(RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer