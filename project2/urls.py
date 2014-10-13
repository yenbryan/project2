from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from project2 import settings
import registration.urls
import discussion.urls
import message.urls

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include(registration.urls)),
    url(r'^message/', include(message.urls)),
    url(r'^discussion/', include(discussion.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^dashboard/$', 'registration.views.dashboard', name='dashboard'),

)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
