from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('Cars',CarViewSet  .as_view({"get":"list"}),name='Cars'),
    path('Cars/Detail',CarListCraeteView .as_view() ,name='Car-Detail' ),
]
