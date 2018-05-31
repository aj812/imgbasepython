from django.conf.urls import url, include
from django.contrib import admin


api_urls = [
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^media/', include('media.urls', namespace='media'))
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]
