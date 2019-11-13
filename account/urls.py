from django.urls import path, include
from account.views import AccountDetail, AccountList

urlpatterns = [
    path('account/', AccountList.as_view()),
    path('account/<str:user_id>', AccountDetail.as_view()),
]
