from django.urls import path

from .views import hello, index, hello1, login, add, redirect_to_index

urlpatterns = [
    path('', redirect_to_index),
    path('hello/', hello, name="hello"),
    path('hello1/<int:sss>', hello1, name="hello1"),
    path('index/', index, name="index"),
    path('login/', login, name="login"),
    path('add/', add, name="add"),
]
