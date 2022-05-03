from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customers', CustomerViewSet, base_name='customers')
router.register('accounts', AccountViewSet, base_name='accounts')
#router.register('transaction', transaction, base_name='transaction')
urlpatterns = [
    path('transaction/', Transaction.as_view()),
    path('', home),
]


urlpatterns += router.urls