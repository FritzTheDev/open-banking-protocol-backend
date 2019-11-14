from .serializers import AccountSerializer
from .models import Account
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import Http404
from rest_framework.response import Response
from django.utils.timezone import datetime
# Create your views here.
# class AccountViewSet(ModelViewSet):
#   """
#   This view gives me retrieve, list, create, update, and delete actions. 
  
#   Use PUT to create new accounts at a specific ID, not POST to create new ones from scratch
#   """
#   queryset = Account.objects.all()
#   serializer_class = AccountSerializer


class AccountList(ListCreateAPIView):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer

class AccountDetail(RetrieveUpdateDestroyAPIView):
  queryset = Account.objects.all()
  lookup_field = 'user_id'
  serializer_class = AccountSerializer

class AccountCheckFundsAvailable(APIView):
  """
  Checks if the matching account in 
  """
  def get(self, request, user_id):
    account = Account.objects.get(user_id=user_id)
    amountParam = request.GET.get('amount')
    currencyParam = request.GET.get('currency')
    now=str(datetime.now())
    if account.balance_currency == currencyParam and float(account.balance_amount) > float(amountParam):
      # Currency matches & has enough money
      return Response({ "answer": "yes", "date": now }, content_type='application/json')
    else:
      # Not enough money in the account or wrong currency type
      return Response({ "answer": "no", "date": now }, content_type='application/json')
    