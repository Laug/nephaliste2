# coding=utf8
from django.db.models import *
from django.contrib.auth.models import User

class Consumer(Model):
	"""
	Non-auth-related data about a client
	"""
	user = OneToOneField(User)
	surnom = CharField(max_length=50, blank=True)
	solde = DecimalField(max_digits=5, decimal_places=2, default=0)
	caution = BooleanField()

	promotion = IntegerField(blank=True, null=True)

	def __unicode__(self):
		return self.user.__unicode__()

	def can_afford(self, amount):
		return ((not self.user.is_active)
				and ((self.user.is_staff)
					or (self.user.solde - amount > -25 and self.caution)
					or (self.user.solde - amount > 0)))


class Credit(Model):
	user = ForeignKey(Consumer)
	date = DateTimeField(auto_now_add=True)
	amount = DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return u"Dépôt de {0}€ par {1} le {2}".format(amount, user, date)

	def save(self, *args, **kwargs):
		self.user.solde += self.amount
		super(Credit, self).save(*args, **kwargs)
		self.user.save()
