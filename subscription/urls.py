from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'$', 'subscription.views.new', name='new'),
)
