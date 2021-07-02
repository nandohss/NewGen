from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import Cliente
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import sys

# Create your views here.

def home(request):
    return render(request, 'home.html')

def loginUser(request):
    return render(request, 'loginUser.html')

def loginSystem(request):
    return render(request, 'loginSystem.html')

# def registrarUsuario(request):
#     """ form = FormClienteForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context= {'form': form }

#     return render(request, 'regUsers.html', context) """

#     if request.method == "POST":
#         form = FormClienteForm(request.POST)
#         """ if form.is_valid():
#             form.save()
#             return redirect('loginSystem')
#         else:
#             messages.error(request, 'Formulário inválido!')
#             return redirect('registrarUsuario') """
#         form.save()
#         return redirect('loginSystem')
#     else:
#         form = FormClienteForm
#         return render(request, 'regUsers.html', {'form': form})

# def registrarUsuario(request, template_name="regUsers.html"):
#     form = FormClienteForm(request.POST or None)
#     if form.is_valid():
#         usuario = form.save(commit=False)
#         usuario.senha = make_password(request.POST['senha'])
#         usuario.save()
#         return redirect('loginSystem')
#     return render(request, template_name, {'form':form})

def registrarUsuario(request, template_name="regUsers.html"):
    print("Antes do if", file=sys.stderr)
    cliente = request.user
    if request.method == "POST":
        nome = request.POST['nome']
        cpf_cnpj = request.POST['cpf_cnpj']
        data_nascimento = request.POST['data_nascimento']
        genero = request.POST['genero']
        email = request.POST['email']
        telefone = request.POST['telefone']
        logradouro = request.POST['logradouro']
        numero = request.POST['numero']
        bairro = request.POST['bairro']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        cep = request.POST['cep']
        senha = request.POST['senha']

        print("Dentro do if", file=sys.stderr)

        cliente = Cliente.objects.create_user(nome, cpf_cnpj, data_nascimento,
        genero, email, telefone, logradouro, numero, bairro, cidade, estado, 
        cep, senha)
        cliente.save()
        return redirect('loginSystem')
    else:
        form = FormClienteForm
        return render(request, 'regUsers.html', {'form': form})

""" if tipo == "administrador":
        cliente = Cliente.objects.create_user
        (username, email, password)
        cliente.is_staff = True
        cliente.save()
    else: """
    

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
