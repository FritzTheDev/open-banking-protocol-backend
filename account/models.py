from django.db.models import Model, CharField

# Create your models here.
class Account(Model):
  """
  ## Account Model
  Contains following data
  - user_id: str (Max 255 char && unique)
  - label: str (Max 255 char)
  - type: str (see docs for Product.product_code) (using account_type to avoid keyword)
  - balance: dict (keys: "currency": str && "amount": str (amount MUST BE 0))
  - branch_id: str
  - account_routing: dict (keys: "scheme": str && "address": str)

  #### NOT (YET) IMPLEMENTED ###
  - account_attributes: list of AccountAttributes. AccountAttributes are
  automatically assigned based on the product_code specified in account_type member
  """


  user_id = CharField(max_length=255)
  label = CharField(max_length=255)
  account_type = CharField(max_length=10)
  balance_currency = CharField(max_length=3)
  balance_amount = CharField(default=0, max_length=20)
  branch_id = CharField(max_length=20)
  account_routing_scheme = CharField(max_length=30)
  account_routing_address = CharField(max_length=30)
