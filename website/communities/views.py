from django.shortcuts import render, render_to_response
from .models import *
from django.template import RequestContext


# Create your views here.

def communities_list(request):
    template_name = 'community_list.html'
    community_list = Community.objects.all()
    return render_to_response(template_name, {"community_list": community_list},
                              context_instance=RequestContext(request))


def index(request):
    return communities_list(request)


def detail(request, community_id):
    template_name = 'community_detail.html'
    community = Community.objects.get(pk=community_id)
    return render_to_response(template_name, {"community": community})
