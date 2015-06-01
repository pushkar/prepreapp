from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'predict.views.index', name='index'),
    url(r'^predict/', include('predict.urls', namespace="predict")),
    url(r'^admin/', include(admin.site.urls)),
)
