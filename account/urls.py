from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import AccountViewSet

router = DefaultRouter()
router.register('accounts', AccountViewSet)

urlpatterns = [
    path('', include(router.urls))
]
