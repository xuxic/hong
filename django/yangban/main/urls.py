from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'vote', views.vote, name='vote'),
    url(r'mmmm', views.mmmm, name='mmmm'),
)