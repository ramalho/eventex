from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.homepage', name='homepage'),
    (r'^inscricao/', include('subscription.urls', namespace='subscription')),
)

urlpatterns += staticfiles_urlpatterns()