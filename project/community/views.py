from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import CommunitySerializer

def community_list(request):
    template_name = 'community/list.html'
    paginator = Paginator(Community.objects.all(), 5)

    try:
        items = paginator.page(request.GET.get('page'))
    except (PageNotAnInteger, EmptyPage):
        items = paginator.page(1)

    return render(request, template_name, {"community_list": items})


def detail(request, pk):
    template_name = 'community/detail.html'
    community = Community.objects.get(pk=pk)
    return render(request, template_name, {"community": community})

class CommunityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows communities to be viewed.
    """
    queryset = Community.objects.all().order_by('-created_date')
    serializer_class = CommunitySerializer