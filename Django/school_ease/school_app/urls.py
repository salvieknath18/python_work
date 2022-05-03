from django.urls import path
from school_app.views import *
from rest_framework.routers import DefaultRouter
from .views import TutorViewSet, TutorList

router = DefaultRouter()
router.register('school_app', TutorViewSet, base_name='Tutors')

urlpatterns = [
    path('', home, name='home_page'),
    path("tutors/", TutorList.as_view(), name="tutor_list"),
    ]
urlpatterns += router.urls
