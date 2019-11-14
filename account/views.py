from .serializers import AccountSerializer
from .models import Account
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import Http404
from rest_framework.response import Response
from django.utils.timezone import datetime


class AccountList(ListCreateAPIView):
  """
  Provides List & Create actions associated with the Account model
  """
  queryset = Account.objects.all()
  serializer_class = AccountSerializer

class AccountDetail(RetrieveUpdateDestroyAPIView):
  """
  Provides Retrieve, Update & Destroy actions associated with the Account model
  """
  queryset = Account.objects.all()
  lookup_field = 'user_id'
  serializer_class = AccountSerializer

class AccountCheckFundsAvailable(APIView):
  """
  Checks if the matching account has sufficient funds & is the right currency.
  """

  def get(self, request, **kwargs):
    account = Account.objects.get(user_id=kwargs['user_id'])
    amountParam = request.GET.get('amount')
    currencyParam = request.GET.get('currency')
    now=str(datetime.now())
    
    if account.balance_currency == currencyParam and float(account.balance_amount) > float(amountParam):
      # Currency matches & has enough money
      return Response({ "answer": "yes", "date": now })
    else:
      # Not enough money in the account or wrong currency type
      return Response({ "answer": "no", "date": now })
    