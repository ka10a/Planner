from django.urls import path

from .views import hello, index, hello1, login

urlpatterns = [
    path('hello/', hello, name="hello"),
    path('hello1/<int:sss>', hello1, name="hello1"),
    path('index/', index, name="index"),
    path('index/login/', login, name="login"),
]
