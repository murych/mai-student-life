from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import *


def community_list(request):
    template_name = 'community/list.html'
    paginator = Paginator(Community.objects.all(), 5)

    try:
        items = paginator.page(request.GET.get('page'))
    except (PageNotAnInteger, EmptyPage):
        items = paginator.page(1)

    return render(request, template_name, {"community_list": items})


def detail(request, community_id):
    template_name = 'community/detail.html'
    community = Community.objects.get(pk=community_id)
    return render(request, template_name, {"community": community})
