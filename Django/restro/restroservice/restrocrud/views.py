from rest_framework import viewsets
from .models import Dish, Restaurant,RestaurantReview,Review
from .serviceSerializer import RestaurantSerializer,RestaurantReviewSerializer,DishSerializer,ReviewSerializer,UserSerializer
from django.contrib.auth.models import User


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RestaurantReviewViewSet(viewsets.ModelViewSet):
    queryset = RestaurantReview.objects.all()
    serializer_class = RestaurantReviewSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


'''
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = RestaurantReviewSerializer
'''