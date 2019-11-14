from django.urls import path, include
from account.views import AccountDetail, AccountList, AccountCheckFundsAvailable

urlpatterns = [
    path('account/', AccountList.as_view()),
    path('account/<str:user_id>', AccountDetail.as_view()),
    path('account/<str:user_id>/funds-available', AccountCheckFundsAvailable.as_view())
]
