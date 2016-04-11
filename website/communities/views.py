from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response

from .models import *


def index(request):
    return community_list(request)


def community_list(request):
    template_name = 'community_list.html'
    paginator = Paginator(Community.objects.all(), 3)

    try:
        items = paginator.page(request.GET.get('page'))
    except (PageNotAnInteger, EmptyPage):
        items = paginator.page(1)

    return render_to_response(template_name, {"community_list": items})


def detail(request, community_id):
    template_name = 'community_detail.html'
    community = Community.objects.get(pk=community_id)
    return render_to_response(template_name, {"community": community})
