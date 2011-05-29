from django.conf.urls.defaults import *

from views import SubscriptionCreateView
from views import SubscriptionSuccessView


urlpatterns = patterns('',
    url(r'^$', SubscriptionCreateView.as_view(), name='subscribe'),
    url(r'^(?P<pk>\d+)/sucesso/$', SubscriptionSuccessView.as_view(), name='success'),
)
