from django.db.models import *
from django.contrib.auth.models import User

class Consumer(User):
	"""
	Non-auth-related data about a client
	"""
	user = OneToOneField(User)
	surnom = CharField(max_length=50, blank=True)
	solde = DecimalField(max_digits=5, decimal_places=2, default=0)
	caution = BooleanField()

	promotion = IntegerField(blank=True, null=True)

	def __unicode__(self):
		return __unicode__(user)

	def can_afford(self, amount):
		return ((not self.user.is_active)
				and ((self.user.is_staff)
					or (self.user.solde - amount > -25 and self.caution)
					or (self.user.solde - amount > 0)))
