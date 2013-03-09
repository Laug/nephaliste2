from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, date, timedelta
from exceptions import SoldeInsuffisant

class Consommable(models.Model):
    """
    Each consommable can be sold by la Coopé
    
    >>> conso = Consommable.objects.create(nom="Pinte de Kro", prix="2.00")
    >>> conso
    'Pinte de Kro à 2.00€'

    """

    nom = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    prix = models.DecimalField(max_digits=4, decimal_places=2)

    def __unicode__(self):
        nom = "{0} à {1} €".format(self.nom, self.prix)
        if not self.disponible:
            nom += " (indisponible)"
        return nom

class Vente(models.Model):
    """
    Orders
    """

    user = models.ForeignKey(User)
    consommation = models.ForeignKey('Consommable')
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
    	vente = "{0} par {1}".format(self.consommation.nom, self.user)
        if self.date is not None:
            vente +=  " le {0}".format(self.date)
        return vente

    def clean(self, *args, **kwargs):
        if not self.user.can_afford(self.consommation.prix):
            raise ValidationError("Solde insuffisant")
        if not self.consommation.disponible:
        	raise ValidationError("Consommable non disponible")

    def save(self, *args, **kwargs):
        """
        Recording a sale
        """
        self.user.solde -= self.consommation.prix
        super(Vente, self).save(*args, **kwargs)
        self.user.save()
