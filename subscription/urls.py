from django.conf.urls.defaults import *

from views import SubscriptionCreateView


urlpatterns = patterns('subscription.views',
    url(r'^$', SubscriptionCreateView.as_view(), name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)
