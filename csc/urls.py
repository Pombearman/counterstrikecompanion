from django.conf.urls import patterns, url
from csc import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^/old$', views.mainPage, name='old'),
        )