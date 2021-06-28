from django.shortcuts import render
from .forms import *

# Create your views here.
def loginUser(request):
    return render(request, 'loginUser.html')

def loginSystem(request):
    return render(request, 'loginSystem.html')

def registrarUsuario(request):
    form = FormClienteForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'regUsers.html', context)

def registrarFuncionario(request):
    form = FormFuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'regEmployee.html', context)

def registrarAdministrador(request):
    form = FormFuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'regAdmnistrator.html', context)
