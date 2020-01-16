from datetime import datetime, date, timedelta

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.views.decorators.csrf import csrf

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import *
# from .serializers import ArticleSerializer
#
from django.utils.timezone import get_current_timezone

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .forms import EventForm
from .models import *
from .utils import Calendar

from .models import ToDoItem
import calendar


def index(request):
    return HttpResponse(loader.get_template('index.html').render({}, request))


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar_simple.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def prev_month(d):
    first = d.replace(day=1)
    prev_mon = first - timedelta(days=1)
    month = 'month=' + str(prev_mon.year) + '-' + str(prev_mon.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_mon = last + timedelta(days=1)
    month = 'month=' + str(next_mon.year) + '-' + str(next_mon.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


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


def calendar_view(request, event_id=None):
    return HttpResponse(loader.get_template('calendar_simple.html').render({}, request))


def redirect_to_index(request):
    return redirect(index)


def delete(request):
    current_user = request.user
    ToDoItem.objects.filter(user=current_user.id).delete()
    return redirect(lists)


def lists(request):
    current_user = request.user

    print(request)

    if request.method == 'POST':
        todoitem = ToDoItem.objects.create(name=request.POST['description'],
                                           due_date=request.POST['date'],
                                           category=request.POST['category'],
                                           user=current_user.id)

    data = {
        "categories": [
            "household", "entertaiment", "study", "other"
        ]
    }

    todos_list = ToDoItem.objects.filter(user=current_user.id)

    if len(todos_list):
        data = {
            "todos": list(todos_list.values(
                "name", "done", "due_date", "category"
            )),
            "categories": [
                "household", "entertaiment", "study", "other"
            ]
        }
    return HttpResponse(loader.get_template('todolist.html').render(data, request))
