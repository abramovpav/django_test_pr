from django.conf.urls import patterns, include, url
from articles import views

urlpatterns = patterns('',
    url(r'$', views.UserCountView.as_view(), name='index'),
)
