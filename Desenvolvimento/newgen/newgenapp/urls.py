# application related urls

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('accounts/loginUser', loginUser, name='loginUser'),
    path('accounts/loginSystem', loginSystem, name='loginSystem'),
    path('accounts/registrarUsuario', registrarUsuario, name='registrarUsuario'),
    path('accounts/registrarFuncionario', registrarFuncionario, name='registrarFuncionario'),
    path('accounts/registrarAdmin', registrarAdministrador, name='registrarAdmin'),
    path('accounts/registrarCoworking', registrarCoworking, name='registrarCoworking')
]
