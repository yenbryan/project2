from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^send/$', 'message.views.send_message', name='send_message'),
    url(r'^view/(?P<message_id>\d+)/$', 'message.views.view_message', name='view_message'),
    url(r'^all/$', 'message.views.all_message', name='all_message')
)