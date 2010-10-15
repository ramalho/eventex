from django.conf.urls.defaults import *

urlpatterns = patterns('',

    url(r'^$', 'subscription.views.subscribe', name='subscribe'),

    url(r'^sucesso/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'subscription/success.html'}, name='success'),
)
