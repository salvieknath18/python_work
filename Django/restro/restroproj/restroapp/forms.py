from django.forms import ModelForm
from .models import Restaurant, Dish
from django.contrib.auth.models import User

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('date',)

class DishForm(ModelForm):
  class Meta:
    model = Dish
    exclude = ('date', 'restaurant',)
