from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'community', views.CommunityViewSet)

app_name = 'community'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^list/$', views.community_list, name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]