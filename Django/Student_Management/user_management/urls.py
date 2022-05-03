from django.urls import path
from user_management.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('studentinfo', StudentViewSet, base_name='studentinfo')

urlpatterns = [
    path('', home, name='home_page'),

    path('list', user_list, name='user_list'),
    path('staff_list', staff_list, name='staff_list'),
    path('instructor_list', instructor_list, name='instructor_list'),

    path('add', user_add, name='user_add'),
    path('editp/<int:id>/', profile_edit, name='profile_edit'),
    path('details/<int:id>/', profile_details, name='profile_details'),
    path('delete/<int:id>/', user_delete, name='user_delete'),

    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),

    path('attendance/', student_attendance, name='student_attendance'),
    path('attendance_records/', student_attendance_record, name='student_attendance_record'),
    path('attendance_report/', student_attendance_report, name='student_attendance_report'),

]

urlpatterns += router.urls