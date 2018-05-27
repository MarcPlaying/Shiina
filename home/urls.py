from django.conf.urls import include, url
from . import views

beatmaps = {'747558'}

urlpatterns = [
    url(r'^beatmaps/', views.beatmaps, name='beatmaps'),
    url(r'^new/', views.new, name='new'),
    url(r'^search/', views.search, name='search'),
    url(r'^', views.index, name='index'),
]
