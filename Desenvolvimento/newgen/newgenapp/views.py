from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import Cliente

# Create your views here.

def home(request):
    return render(request, 'home.html')

def loginUser(request):
    return render(request, 'loginUser.html')

def loginSystem(request):
    return render(request, 'loginSystem.html')

def registrarUsuario(request):
    """ form = FormClienteForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'regUsers.html', context) """

    if request.method == "POST":
        form = FormClienteForm(request.POST)
        """ if form.is_valid():
            form.save()
            return redirect('loginSystem')
        else:
            messages.error(request, 'Formulário inválido!')
            return redirect('registrarUsuario') """
        form.save()
        return redirect('loginSystem')
    else:
        form = FormClienteForm
        return render(request, 'regUsers.html', {'form': form})

def registrarFuncionario(request):
    form = FormFuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'regEmployee.html', context)

def registrarCoworking(request):
    form = FormFuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'regCoworking.html', context)

def registrarAdministrador(request):
    form = FormFuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'regAdmin.html', context)
