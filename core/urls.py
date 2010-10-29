from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^palestras/$', 'talks', name='talks'),
    url(r'^palestrante/([-\w]+)/$', 'speaker', name='speaker'),
)
