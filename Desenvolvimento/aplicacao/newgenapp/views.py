from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import Cliente
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, User, UserManager
import sys
from django.urls import reverse
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm, UsernameField
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user

#print("Comentários do console", file=sys.stderr)

# Create your views here.


def home(request):
    return render(request, 'home.html')

def loginUser(request):
    return render(request, 'loginUser.html')

def loginSystem(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            login(request, user)
            grupo = 'grupo'

            l = request.user.groups.values_list('name',flat = True) # QuerySet Object
            # print(f"l = {l}", file=sys.stderr)
            # print(f"user = {user}", file=sys.stderr)
            l_as_list = list(l)
            grupo = str(l_as_list)

            return render(request, 'home.html', {'grupo': grupo})

    else:
        form = AuthenticationForm()
    return render(request, 'loginSystem.html', {'form': form})

def escolherCadastro(request):
    contexto = {}
    return render(request, 'escolherCadastro.html', contexto)

def registrarUsuario(request):
    if request.method == "POST":
        cliente = FormClienteForm(request.POST)
        if cliente.is_valid():
            cpf_cnpj = request.POST['cpf_cnpj']
            email = request.POST['email']
            senha = request.POST['senha']

            # Regras de negócio de detecção se o cliente é empresa ou pessoa
            # (se == 11 então = cpf, senão, cnpj)
            if len(cpf_cnpj) == 11:
                my_group = Group.objects.get(name='clientePessoa')
                nome = request.POST['nome'].capitalize().strip()
                nome = nome.split(' ')
                first_name = nome[0]
                nome.pop(0)
                last_name = ' '.join(nome)

            else:
                my_group = Group.objects.get(name='clienteEmpresa')
                first_name = request.POST['nome'].capitalize().strip()
                last_name = ''
            
            # Salva na tabela user
            user = User.objects.create_user(username=cpf_cnpj, password=senha,
             email=email, first_name=first_name, last_name=last_name)
            user.save()

            # Salva na tabela cliente
            cliente.save()

            # Configura um grupo de acesso para o usuário            
            my_group.user_set.add(user)

            return redirect('loginSystem')
        else:
            messages.error(request, 'Formulário inválido!')
            return redirect('registrarUsuario')
    else:
        form = FormClienteForm
        return render(request, 'regUsers.html', {'form': form})
    
def registrarFuncionario(request):
    """ form = FormFuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'regEmployee.html', context) """
    if request.method == "POST":
        funcionario = FormFuncionariosForm(request.POST)
        if funcionario.is_valid():
            cpf_cnpj = request.POST['cpf_cnpj']
            email = request.POST['email']
            senha = request.POST['senha']

            my_group = Group.objects.get(name='funcionario')
            nome = request.POST['nome'].capitalize().strip()
            nome = nome.split(' ')
            first_name = nome[0]
            nome.pop(0)
            last_name = ' '.join(nome)
            
            # Salva na tabela user
            user = User.objects.create_user(username=cpf_cnpj, password=senha,
             email=email, first_name=first_name, last_name=last_name, is_staff=True)
            user.save()

            # Salva na tabela funcionario
            funcionario.save()

            # Configura um grupo de acesso para o usuário            
            my_group.user_set.add(user)

            return redirect('loginSystem')
        else:
            messages.error(request, 'Formulário inválido!')
            return redirect('registrarUsuario')
    else:
        form = FormFuncionariosForm
        return render(request, 'regUsers.html', {'form': form})

# def registrarCoworking(request):
    form = FormFuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'regCoworking.html', context)

def registrarAdministrador(request):
    """ form = FormFuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form } """
    if request.method == "POST":
        funcionario = FormRegistrarAdministrador(request.POST)
        if funcionario.is_valid():
            cpf_cnpj = request.POST['cpf_cnpj']
            email = request.POST['email']
            senha = request.POST['senha']

            my_group = Group.objects.get(name='administrador')
            first_name = request.POST['nome'].capitalize().strip()
            last_name = ''
            
            # Salva na tabela user
            user = User.objects.create_user(username=cpf_cnpj, password=senha,
             email=email, first_name=first_name, last_name=last_name, is_superuser=True,
             is_staff=True)
            user.save()

            # Salva na tabela funcionario
            funcionario.save()

            # Configura um grupo de acesso para o usuário            
            my_group.user_set.add(user)

            return redirect('loginSystem')
        else:
            messages.error(request, 'Formulário inválido!')
            return redirect('registrarUsuario')
    else:
        form = FormRegistrarAdministrador
        return render(request, 'regAdministrator.html', {'form': form})




# def registrarUsuario(request, template_name="regUsers.html"):
#     form = FormClienteForm(request.POST or None)
#     if form.is_valid():
#         usuario = form.save(commit=False)
#         usuario.senha = make_password(request.POST['senha'])
#         usuario.save()
#         return redirect('loginSystem')
#     return render(request, template_name, {'form':form})

# def registrarUsuario(request, template_name="regUsers.html"):
#     print("Antes do if", file=sys.stderr)
#     cliente = request.user
#     if request.method == "POST":
#         nome = request.POST['nome']
#         cpf_cnpj = request.POST['cpf_cnpj']
#         data_nascimento = request.POST['data_nascimento']
#         genero = request.POST['genero']
#         email = request.POST['email']
#         telefone = request.POST['telefone']
#         logradouro = request.POST['logradouro']
#         numero = request.POST['numero']
#         bairro = request.POST['bairro']
#         cidade = request.POST['cidade']
#         estado = request.POST['estado']
#         cep = request.POST['cep']
#         senha = request.POST['senha']

#         print("Dentro do if", file=sys.stderr)

#         cliente = Cliente.objects.create_user(nome, cpf_cnpj, data_nascimento,
#         genero, email, telefone, logradouro, numero, bairro, cidade, estado, 
#         cep, senha)
#         cliente.save()
#         return redirect('loginSystem')
#     else:
#         form = FormClienteForm
#         return render(request, 'regUsers.html', {'form': form})

# """ if tipo == "administrador":
#         cliente = Cliente.objects.create_user
#         (username, email, password)
#         cliente.is_staff = True
#         cliente.save()
#     else: """

    """ form = FormClienteForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form }

    return render(request, 'regUsers.html', context) """