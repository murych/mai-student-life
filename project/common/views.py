from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


def index(request):
    return redirect(reverse('community:list'))


def about(request):
    template_name = 'common/about.html'
    return render(request, template_name)
