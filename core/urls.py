from django.conf.urls.defaults import patterns, url
from views import HomepageView
from views import TalkListView
from views import TalkDetailView

urlpatterns = patterns('core.views',
    url(r'^palestrante/([-\w]+)/$', 'speaker', name='speaker'),
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^palestras/$', TalkListView.as_view(), name='talks'),
    url(r'^palestras/(?P<pk>\d+)/$', TalkDetailView.as_view(), name='talk_details'),
)
