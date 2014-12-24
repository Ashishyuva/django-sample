from django.conf.urls import patterns, url, include
from home import views

urlpatterns = patterns('',
   # ex: /polls/
   
    url(r'^$', views.index, name='index'),
)