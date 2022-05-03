from django.urls import path,include, re_path
from .views import *



urlpatterns = [
    path('',homepage),
    path('restaurants/',restaurants),
    path(r'restaurantCRUD/<str:urlmethod>/<int:id>/',restaurantsCRUD),
    path('dishes/',dishes),
    path(r'dishesCRUD/<str:urlmethod>/<int:id>/',dishesCRUD),
    path(r'restaurantReview/<int:id>/',restaurantReview)
]
