from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'$', 'subscription.views.subscribe', name='subscribe'),
)
