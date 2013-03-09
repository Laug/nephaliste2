from django.db.models import *
from django.contrib.auth.models import User

class Consumer(User):
	"""
	Non-auth-related data about a client
	"""
	user = OneToOneField(User)
	surnom = CharField(max_length=50, blank=True)
	solde = DecimalField(max_digits=5, decimal_places=2, default=0)
	caution = DateField(blank=True, null=True)

	promotion = IntegerField(blank=True, null=True)
