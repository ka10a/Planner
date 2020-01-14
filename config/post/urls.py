from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index, login, add, redirect_to_index, lists, calendar

urlpatterns = [
    path('', redirect_to_index),
    path('index/', index, name="index"),
    path('login/', login, name="login"),
    path('add/', add, name="add"),
    path('lists/', lists, name="lists"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('calendar/', calendar, name='calendar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
