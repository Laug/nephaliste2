from django.conf.urls import patterns, include, url

urlpatterns = patterns('gestion.views',
	url(r'^debiter/$', 'debit'),
	url(r'^crediter/$', 'credit'),
)
