from django.urls import path
from .views import polls_list1, polls_detail1, PollViewSet, UserCreate, LoginView
from .views import PollList2, PollDetail2, PollList3, PollDetail3, ChoiceList, CreateVote
from rest_framework.routers import DefaultRouter

#from rest_framework.authtoken import views

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')


urlpatterns = [

    # **********   Poll Urls 3 designs **************
    # Sending response Without Serializer need to add followings
    path("polls1/", polls_list1, name="polls_list"),
    path("polls1/<int:pk>/", polls_detail1, name="polls_detail"),


    # Sending response with serializer
    path("polls2/", PollList2.as_view(), name="polls_list"),
    path("polls2/<int:pk>/", PollDetail2.as_view(), name="polls_detail"),


    # Sending response with serializer
    # allowed only GET, POST, HEAD, OPTIONS for following
    path("polls3/", PollList3.as_view(), name="polls_list"),
    # allowed only GET, DELETE, HEAD, OPTIONS for following
    path("polls3/<int:pk>/", PollDetail3.as_view(), name="polls_detail"),



    # allowed only GET, POST, HEAD, OPTIONS for following
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),

    # allowed only post and option for following
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    # another way to obtain auth token
    #path("login2/", views.obtain_auth_token, name="login"),
]


urlpatterns += router.urls