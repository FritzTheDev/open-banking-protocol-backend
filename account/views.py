from .serializers import AccountSerializer
from .models import Account
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

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

class AccountDetail(RetrieveAPIView):
  queryset = Account.objects.all()
  lookup_field = 'user_id'
  serializer_class = AccountSerializer
  