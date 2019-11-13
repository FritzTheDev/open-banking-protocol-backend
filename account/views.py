from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import AccountSerializer
from .models import Account

# Create your views here.
class AccountViewSet(ReadOnlyModelViewSet):
  """
  ### AccountViewSet
  This viewset automatically gives me "list" & 
  "detail" api views, or "actions", if you will.
  """
  queryset = Account.objects.all()
  serializer_class = AccountSerializer