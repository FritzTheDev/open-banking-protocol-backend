from rest_framework.viewsets import ModelViewSet
from .serializers import AccountSerializer
from .models import Account

# Create your views here.
class AccountViewSet(ModelViewSet):
  """
  This view gives me retrieve, list, create, update, and delete actions. 
  
  Use PUT to create new accounts at a specific ID, not POST to create new ones from scratch
  """
  queryset = Account.objects.all()
  serializer_class = AccountSerializer