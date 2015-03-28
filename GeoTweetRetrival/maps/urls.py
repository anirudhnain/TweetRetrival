from django.conf.urls import patterns, url
from maps import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'map/', views.search, name='search'))