from django.conf.urls import patterns, url

from webapp import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^dashboard/$', views.dashboard),
    url(r'^refresh/$', views.refresh),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
)
