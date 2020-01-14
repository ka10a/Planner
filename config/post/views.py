from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

def index(request):
    return HttpResponse(loader.get_template('index.html').render({}, request))


def login(request):
    return HttpResponse(loader.get_template('login.html').render({}, request))


def add(request):
    return HttpResponse(loader.get_template('add.html').render({}, request))


def redirect_to_index(request):
    return redirect(index)

def lists(request):
    return HttpResponse(loader.get_template('todolist.html').render({}, request))
