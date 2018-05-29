from django.conf.urls import url, include
from django.contrib import admin


api_urls = [
    url(r'^users/', include('users.urls')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),

]

# from django.conf.urls import url, include
# from rest_framework import routers
# from api import views
#
# router = routers.DefaultRouter()
# router.register(r'^api/', include('api.urls', namespace='api'))
# # router.register(r'groups', views.GroupViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
