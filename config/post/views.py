from django.http import HttpResponse
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


def index(request):
    return HttpResponse(loader.get_template('index.html').render({}, request))

def deletecal(request):
    return HttpResponse(loader.get_template('deletecal.html').render({}, request))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # TODO: change index to the right page
            return redirect('calendar')
    else:
        form = UserCreationForm()
    return HttpResponse(loader.get_template('add.html').render({
        'form': form
    }, request))

#     c = {}
#     c.update(csrf(request))
#     return render(request, 'login.html', c)


def login(request):
    form = UserCreationForm()
    return HttpResponse(loader.get_template('login.html').render({
        'form': form
    }, request))


def calendar(request):
    return HttpResponse(loader.get_template('calendar_simple.html').render({}, request))


# def auth(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             # ...
#             # TODO: replace 'login.html' to right page
#             return HttpResponse(loader.get_template('login.html').render({}, request))
#         else:
#             return HttpResponse(loader.get_template('login.html').render({}, request))
#             # Return an 'invalid login' error message.
#             # ...
#     else:
#         return HttpResponse(loader.get_template('login.html').render({}, request))


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


# def add(request):
#     return HttpResponse(loader.get_template('add.html').render({}, request))


def redirect_to_index(request):
    return redirect(index)

def lists(request):
    return HttpResponse(loader.get_template('todolist.html').render({}, request))
