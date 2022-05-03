from django.urls import  path
from poll.views import *

urlpatterns = [
    path('', index, name='polls_list'),
    path('<int:id>/', details, name='poll_details' ),
    path('<int:id>/ans/', poll_ans, name='poll_answer' )
]