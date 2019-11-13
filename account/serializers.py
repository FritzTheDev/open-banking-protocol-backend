from rest_framework.serializers import ModelSerializer, CharField
from account.models import Account

class AccountSerializer(ModelSerializer):
  class Meta:
    model = Account
    fields = ['user_id', 'label', 'account_type', 'balance_currency', 'balance_amount', 'branch_id', 'account_routing_scheme', 'account_routing_address']
