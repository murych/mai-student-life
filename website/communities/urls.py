from django.conf.urls import url

from . import views

app_name = 'communities'
urlpatterns = [
    url(r'^$', views.index, name='community_index'),
    url(r'^communities/$', views.community_list, name='community_list'),
    url(r'^communities/(?P<community_id>[0-9]+)/$', views.detail, name='community_detail'),
]
