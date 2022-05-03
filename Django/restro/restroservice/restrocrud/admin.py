from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Review, Dish,RestaurantReview,Restaurant


admin.site.register(RestaurantReview)
admin.site.register(Restaurant)
#admin.site.register(Review)
admin.site.register(Dish)
