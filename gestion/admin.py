#encoding=utf-8
from django.contrib import admin
from models import *
from forms import DebitForm

class ConsommableAdmin(admin.ModelAdmin):
        list_display = ("nom", "prix", "disponible")

class VenteAdmin(admin.ModelAdmin):
        list_display = ("user", "consommation", "date")
        form = DebitForm

admin.site.register(Consommable, ConsommableAdmin)
admin.site.register(Vente, VenteAdmin)
