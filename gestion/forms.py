from django.forms import ModelForm, ModelChoiceField
from models import Vente
from consumer.models import Credit

class DebitForm(ModelForm):
	class Meta:
		model = Vente

class CreditForm(ModelForm):
	class Meta:
		model = Credit