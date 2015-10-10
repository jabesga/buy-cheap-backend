from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/v1/', include('api.urls')),
                       #url(r'^router/', include(router.urls)),
                       #url(r'^quickstart/', include('quickstart.urls')),
                       #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       )