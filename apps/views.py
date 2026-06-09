from django.shortcuts import render
from rest_framework import viewsets,generics
from apps.models import *
from .serializers import *
from drf_spectacular.utils import extend_schema, extend_schema_view
@extend_schema(tags=['Auth'])
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
class CarListCraeteView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


