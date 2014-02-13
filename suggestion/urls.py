from django.conf.urls import patterns, url

urlpatterns = patterns('suggestion.views',
        url(r'^$', 'index'),
        )

