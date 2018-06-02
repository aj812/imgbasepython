from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'media'

urlpatterns = [
    url(r'^$', views.MediaCreateAPIView.as_view(), name="list"),
    url(r'^(?P<pk>[0-9]+)/$', views.MediaDetailAPIView.as_view(), name="detail"),
    url(r'^search/$', views.SearchImgsView, name="search"),
    # url(r'^search/(?P<tags>[a-z]+)/$', views.SearchImgsView, name="search"),
]
