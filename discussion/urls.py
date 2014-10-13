from django.conf.urls import patterns, include, url
from registration.forms import LoginForm, ResetPWord


urlpatterns = patterns('',

    url(r'^post-discussion/$', 'discussion.views.post_discussion', name='post_discussion'),
    url(r'^$', 'discussion.views.discussions', name='discussions'),
    url(r'^view-discussion/(?P<discussion_id>\d+)/$', 'discussion.views.view_discussion', name='view_discussion'),
    url(r'^add-comment/(?P<discussion_id>\d+)/$', 'discussion.views.add_comment', name='add_comment'),
    url(r'^add-discussion/$', 'discussion.views.add_discussion', name='add_discussion'),

)