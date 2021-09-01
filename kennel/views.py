from django.shortcuts import render
from rest_framework import generics
from .serializers import KennelSerializer
from .models import Kennel

# Create your views here.
class KennelView(generics.CreateAPIView):
    queryset = Kennel.objects.all()
    serializer_class = KennelSerializer