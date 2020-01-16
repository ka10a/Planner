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


def deletecal(request):
    return HttpResponse(loader.get_template('deletecal.html').render({}, request))


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar_simple.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        # context['prev_month'] = prev_month(d)
        # context['next_month'] = next_month(d)
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
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponse(loader.get_template('calendar_simple.html').render({}, request))
    return HttpResponse(loader.get_template('calendar_simple.html').render({'form': form}, request))


def hello(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render({'ty': 'pidor'}, request))


def hello1(request, sss):
    template = loader.get_template('hello1.html')
    context = {
        'number': sss,
    }
    return HttpResponse(template.render(context, request))


def redirect_to_index(request):
    return redirect(index)


def lists(request):
    if request.method == 'POST':
        todoitem = ToDoItem.objects.create(name=request.POST['description'],
                                           due_date=request.POST['date'],
                                           category=request.POST['category'])

    todos_list = ToDoItem.objects.all()
    data = {
        "todos": list(todos_list.values(
            "name", "done", "due_date", "category"
        )),
        "categories": [
            "household", "entertaiment", "study", "other"
        ]
    }
    return HttpResponse(loader.get_template('todolist.html').render(data, request))
