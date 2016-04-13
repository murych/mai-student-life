from django.conf.urls import url

from . import views

app_name = 'community'
urlpatterns = [
    url(r'^list/$', views.community_list, name='list'),
    url(r'^detail/(?P<community_id>[0-9]+)/$', views.detail, name='detail'),
]
