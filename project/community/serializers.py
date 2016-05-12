from .models import Community
from rest_framework import serializers
from django.core.urlresolvers import reverse

class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='community:detail',
        lookup_field='pk'
    )
    class Meta:
        model = Community
        fields = ('pk', 'url', 'created_date', 'title','description','vk_link','contacts','community_type')