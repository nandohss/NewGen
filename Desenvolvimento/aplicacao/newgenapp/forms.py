from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from django.contrib.auth.models import User
from .models import *
""" from input_mask.widgets import InputMask
from django_localflavor_br.forms import BRCPFField, BRPhoneNumberField
from input_mask.contrib.localflavor.br.widgets import BRCPFInput, BRPhoneNumberInput """


""" class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] """

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'required': 'true'}), label="cpf/cnpj")
#     senha = forms.CharField(widget=forms.PasswordInput(
#         attrs={'required': 'true', 'minlength': '6'}))

#     class Meta:
#         model = User
#         fields = ['username', 'password']


class FormRegistrarAdministrador(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(
        attrs={'required': 'true'}), label="Nome Social")
    cpf_cnpj = forms.CharField(widget=forms.TextInput(
        attrs={'required': 'true'}), label="CNPJ", max_length=14)
    logradouro = forms.CharField(widget=forms.TextInput(
            attrs={'required': 'true'}))
    email = forms.EmailField(widget=forms.EmailInput(
            attrs={'required': 'true'}))
    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'required': 'true', 'minlength': '6'}))

    class Meta:
        model= Funcionarios
        fields= ["nome", "senha", "cpf_cnpj", "email", "telefone", "logradouro"]

class FormTipoespacoForm(forms.ModelForm):
    class Meta:
        model= Tipoespaco
        fields= ["descricao", "nome"]

class FormPagamentoForm(forms.ModelForm):
    class Meta:
        model= Pagamento
        fields= ["metodo", "cod_mercadopago", "aprovado"]

class FormEspacosForm(forms.ModelForm):
    class Meta:
        model= Espacos
        fields= ["id_tipo_espaco", "preco"]

class FormEquipamentosForm(forms.ModelForm):
    class Meta:
        model= Equipamentos
        fields= ["tipo", "descrição", "preco"]

class FormClienteForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(
        attrs={'required': 'true'}), label="Nome Completo")
    # cpf = BRCPFField(widget= BRCPFInput(
    #         attrs={'class': 'form-control','data-mask': '000.000.000-00', 'required': 'true'}), label="CPF")
    # data_nascimento = forms.DateField(widget=DataCustomInput(
    #         attrs={'class': 'form-control', 'data-mask': '00/00/0000', 'required': 'true'}), label="Data de Nascimento")
    genero = forms.Select(
        attrs={'required': 'false'})
    # telefone = forms.(widget=BRPhoneNumberInput(
    #         attrs={'class': 'form-control', 'data-mask': '(00) 00000-0000', 'required': 'true'}))
    logradouro = forms.CharField(widget=forms.TextInput(
            attrs={'required': 'true'}))
    estado = forms.Select(
        attrs={'required': 'true'})
    cidade = forms.CharField(widget=forms.TextInput(
            attrs={'required': 'true'}))
    
    email = forms.EmailField(widget=forms.EmailInput(
            attrs={'required': 'true'}))
    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'required': 'true', 'minlength': '6'}))

    class Meta:
        model= Cliente
        fields= ["nome", "senha", "cpf_cnpj", "data_nascimento", "genero", "email", "telefone", "logradouro", "numero", "bairro", "cidade", "estado", "cep"]

class FormFuncionariosForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(
        attrs={'required': 'true'}), label="Nome Completo")
    genero = forms.Select(
        attrs={'required': 'false'})
    logradouro = forms.CharField(widget=forms.TextInput(
            attrs={'required': 'true'}))
    estado = forms.Select(
        attrs={'required': 'true'})
    cidade = forms.CharField(widget=forms.TextInput(
            attrs={'required': 'true'}))
    email = forms.EmailField(widget=forms.EmailInput(
            attrs={'required': 'true'}))
    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'required': 'true', 'minlength': '6'}))

    class Meta:
        model= Funcionarios
        fields= ["nome", "senha", "cpf_cnpj", "data_nascimento", "genero", "email", "telefone", "logradouro", "numero", "bairro", "cidade", "estado", "cep"]

class FormPacoteHorasForm(forms.ModelForm):
    class Meta:
        model= Pacotehoras
        fields= ["id_cliente", "qtd_horas", "id_empresa"]

class FormReservaForm(forms.ModelForm):
    class Meta:
        model= Reserva
        fields= ["id_cliente", "id_pagamento", "data_log", "hora_log", "id_espaco", "id_pacote_horas", "id_empresa", "data_reserva", "hora_entrada", "hora_saida", "hora_limpeza"]

class FormAdvertenciaForm(forms.ModelForm):
    class Meta:
        model= Advertencias
        fields= ["comentario", "id_reserva", "id_funcionario"]

class FormConvidadosForm(forms.ModelForm):
    class Meta:
        model= Convidados
        fields= ["id_reserva", "id_cliente"]

class FormEquipamentoreservaForm(forms.ModelForm):
    class Meta:
        model= Equipamentoreserva
        fields= ["id_reserva", "id_equipamento"]