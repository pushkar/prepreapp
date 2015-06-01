from django.conf.urls import patterns, url

from predict import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/(?P<list_id>[0-9]+)/(?P<action>\w+)/(?P<param1>[0-9]+)/(?P<param2>[0-9]+)/(?P<param3>[0-9]+)$', views.input, name='input'),
    url(r'^out/(?P<user>[0-9]+)$', views.output, name='output'),
    url(r'^populate$', views.populate, name='populate'),
)
