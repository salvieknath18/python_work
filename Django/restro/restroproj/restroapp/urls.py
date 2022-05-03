from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from .models import Restaurant, Dish
from .forms import RestaurantForm, DishForm
from .views import RestaurantCreate, DishCreate, RestaurantDetail, review
import re
from django.conf import settings

#from rest_framework_swagger.views import get_swagger_view
#schema_view = get_swagger_view(title='API name')

app_name="restroapp"

urlpatterns = [
#url(r'^docs/$', schema_view, name="schema_view"), #swagger -- rest api

# List latest 5 restaurants: /restroapp/
    url(r'^$',
        ListView.as_view(
        	queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
        	context_object_name='latest_restaurant_list',
        	template_name='restroapp/restaurant_list.html'),
        name='restaurant_list'),

# Restaurant details, ex.: /restroapp/restaurants/1/
    url(r'\^restaurants/(?P<pk>\d+)/\$',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),

# Restaurant dish details, ex: /restroapp/restaurants/1/dishes/1/
    url(r'\^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/\$',
        DetailView.as_view(
        	model=Dish,
        	template_name='restroapp/dish_detail.html'),
        name='dish_detail'),

# Create a restaurant, /restroapp/restaurants/create/
    url(r'\^restaurants/create/\$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

# Edit restaurant details, ex.: /restroapp/restaurants/1/edit/
    url(r'\^restaurants/(?P<pk>\d+)/edit/\$',
        UpdateView.as_view(
        	model = Restaurant,
        	template_name = 'restroapp/form.html',
        	form_class = RestaurantForm),
            name='restaurant_edit'),

# Create a restaurant dish, ex.: /restroapp/restaurants/1/dishes/create/
    url(r'\^restaurants/(?P<pk>\\d+)/dishes/create/\$',
    	DishCreate.as_view(),
        name='dish_create'),

# Edit restaurant dish details, ex.: /restroapp/restaurants/1/dishes/1/edit/
    url(r'\^restaurants/(?P<pkr>\\d+)/dishes/(?P<pk>\\d+)/edit/\$',
    	UpdateView.as_view(
    		model = Dish,
    		template_name = 'restroapp/form.html',
    		form_class = DishForm),
    	name='dish_edit'),

# Create a restaurant review, ex.: /restroapp/restaurants/1/reviews/create/
# Unlike the previous patterns, this one is implemented using a method view instead of a class view
    url(r'\^restaurants/(?P<pk>\\d+)/reviews/create/\$',
    	review,
    	name='review_create'),

]

'''
if settings.DEBUG:
    urlpatterns += url(r'\^media/(?P<path>.\*)\$', 'django.views.static.serve',
    		{'document_root': settings.MEDIA_ROOT, }),
'''