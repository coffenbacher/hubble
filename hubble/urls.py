from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hubble.views.home', name='home'),
    url(r'^snapshot/', include('snapshot.urls')),
    url(r'^suggestion/', include('suggestion.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
