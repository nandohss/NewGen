# application related urls

from django.contrib import admin
from django.urls import path, include
from register import views as v
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('register', v.register, name='register'),
    path('accounts/escolherCadastro', escolherCadastro, name='escolherCadastro'),
    path('accounts/loginUser', loginUser, name='loginUser'),
    path('accounts/loginSystem', loginSystem, name='loginSystem'),
    path('accounts/registrarUsuario', registrarUsuario, name='registrarUsuario'),
    path('accounts/registrarFuncionario', registrarFuncionario, name='registrarFuncionario'),
    path('accounts/registrarAdmin', registrarAdministrador, name='registrarAdmin'),
    #path('accounts/registrarCoworking', registrarCoworking, name='registrarCoworking'),

    path('', include('django.contrib.auth.urls')),

]
