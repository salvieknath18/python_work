from rest_framework import routers
from .views import DishViewSet,RestaurantReviewViewSet,RestaurantViewSet,UserViewSet
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API name')




router = routers.DefaultRouter()
router.register(r'dishes', DishViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'restaurantsreviews', RestaurantReviewViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls

urlpatterns = [
    url(r'^docs/$', schema_view, name="schema_view") #swagger -- rest api
]
urlpatterns += router.urls


#pip install django-rest-swagger