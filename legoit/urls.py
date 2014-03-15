from django.conf.urls import patterns, include, url
from django.contrib import admin

from posts.views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)