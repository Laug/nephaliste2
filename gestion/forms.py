from django.forms import ModelForm, ModelChoiceField
from models import *

class DebitForm(ModelForm):
	class Meta:
		model = Vente
