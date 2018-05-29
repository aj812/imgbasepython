from django.urls import path
from django.conf.urls import url

from media.views import views

app_name = 'media'


urlpatterns = [
    path('', views.index, name='index')
]
