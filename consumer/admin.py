from django.contrib import admin
from models import *
from gestion.forms import CreditForm

class CreditAdmin(admin.ModelAdmin):
        list_display = ('user', 'amount', 'date')
        list_display_links = list_display
        form = CreditForm

class ConsumerAdmin(admin.ModelAdmin):
        list_display = ('user', 'solde', 'promotion')

admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(Credit, CreditAdmin)
