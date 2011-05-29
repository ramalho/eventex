from django.conf.urls.defaults import patterns, url
from views import HomepageView
from views import TalkListView
from views import TalkDetailView

urlpatterns = patterns('core.views',
    url(r'^palestras/$', TalkListView.as_view(), name='talks'),
    url(r'^palestras/(?P<pk>\d+)/$', TalkDetailView.as_view(), name='talk_detail'),
    url(r'^palestrante/([-\w]+)/$', 'speaker_detail', name='speaker_detail'),
    url(r'^$', HomepageView.as_view(), name='homepage'),
)
