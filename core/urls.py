from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^palestras/$', 'talks', name='talks'),
    url(r'^palestrante/(\d+)/$', 'speaker', name='speaker'),
)
