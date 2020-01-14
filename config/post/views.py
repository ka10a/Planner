from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader


# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import *
# from .serializers import ArticleSerializer
#

def hello(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render({'ty': 'pidor'}, request))


def hello1(request, sss):
    template = loader.get_template('hello1.html')
    context = {
        'number': sss,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    return HttpResponse(loader.get_template('index.html').render({}, request))


def login(request):
    return HttpResponse(loader.get_template('login.html').render({}, request))


def add(request):
    return HttpResponse(loader.get_template('add.html').render({}, request))


def redirect_to_index(request):
    return redirect(index)
