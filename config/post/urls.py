from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index, login, add, redirect_to_index, lists

urlpatterns = [
    path('', redirect_to_index),
    path('index/', index, name="index"),
    path('login/', login, name="login"),
    path('add/', add, name="add"),
    path('lists/', lists, name="lists"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
