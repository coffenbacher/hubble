from django.conf.urls import patterns, url

urlpatterns = patterns('snapshot.views',
        url(r'^$', 'index'),
        url(r'^(?P<cd>\d+)/suggest/$', 'suggest'),
        url(r'^(?P<cd>\d+)/approve/$', 'approve'),
        )

