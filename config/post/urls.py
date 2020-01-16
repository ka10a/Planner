from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index, login, signup, redirect_to_index, lists, calendar, deletecal, CalendarView, delete

urlpatterns = [
    path('', redirect_to_index),
    path('index/', index, name="index"),
    path('login/', login, name="login"),
    path('add/', signup, name="add"),
    path('lists/', lists, name="lists"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('deletecal/', deletecal, name='deletecal'),
    path('delete/', delete, name='delete')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
