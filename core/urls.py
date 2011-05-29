from django.conf.urls.defaults import patterns, url
from views import HomepageView

urlpatterns = patterns('core.views',
    url(r'^palestras/$', 'talks', name='talks'),
    url(r'^palestra/(\d+)/$', 'talk_details', name='talk_details'),
    url(r'^palestrante/([-\w]+)/$', 'speaker', name='speaker'),
    url(r'^$', HomepageView.as_view(), name='homepage'),
)
