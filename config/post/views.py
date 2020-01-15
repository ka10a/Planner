from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.views.decorators.csrf import csrf

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import *
# from .serializers import ArticleSerializer
#
from .models import ToDoItem


def index(request):
    return HttpResponse(loader.get_template('index.html').render({}, request))

def deletecal(request):
    return HttpResponse(loader.get_template('deletecal.html').render({}, request))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('calendar')
    else:
        form = UserCreationForm()

    return HttpResponse(loader.get_template('add.html').render({
        'form': form
    }, request))


def login(request):
    form = UserCreationForm()
    return HttpResponse(loader.get_template('login.html').render({
        'form': form
    }, request))


def calendar(request):
    return HttpResponse(loader.get_template('calendar_simple.html').render({}, request))


def hello(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render({'ty': 'pidor'}, request))


def hello1(request, sss):
    template = loader.get_template('hello1.html')
    context = {
        'number': sss,
    }
    return HttpResponse(template.render(context, request))


# def add(request):
#     return HttpResponse(loader.get_template('add.html').render({}, request))


def redirect_to_index(request):
    return redirect(index)


def lists(request):
    if request.method == 'POST':
        pass

    todos_list = ToDoItem.objects.all()
    data = {
        "todos": list(todos_list.values(
            "name", "todo", "done", "created", "due_date", "category"
        )),
        "categories": [
            "household", "entertaiment", "study", "other"
        ]
    }
    return HttpResponse(loader.get_template('todolist.html').render(data, request))
