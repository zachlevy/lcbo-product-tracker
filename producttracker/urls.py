from django.conf.urls import patterns, url

from producttracker import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)