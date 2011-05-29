from django.conf.urls.defaults import patterns, url
from views import HomepageView
from views import TalkListView

urlpatterns = patterns('core.views',
    url(r'^palestras/$', TalkListView.as_view(), name='talks'),
    url(r'^palestra/(\d+)/$', 'talk_detail', name='talk_detail'),
    url(r'^palestrante/([-\w]+)/$', 'speaker_detail', name='speaker_detail'),
    url(r'^$', HomepageView.as_view(), name='homepage'),
)
