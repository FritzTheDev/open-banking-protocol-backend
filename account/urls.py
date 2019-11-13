from django.urls import path, include
from account.views import AccountDetail, AccountList

urlpatterns = [
    path('', AccountList),
    path('<str: user_id>', AccountDetail),
]
