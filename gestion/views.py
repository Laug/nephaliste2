from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from forms import *

def debit(request):
	if request.method == 'POST':
		form = DebitForm(request.POST)
		if form.is_valid():
			conso = form.save()
	else:
		form = DebitForm()

	return render(request, 'gestion/debit.html', {
		'form': form
		})

def credit(request):
	if request.method == 'POST':
		form = CreditForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			conso = form.save()
	else:
		form = CreditForm()

	return render(request, 'gestion/credit.html', {
		'form': form
		})
