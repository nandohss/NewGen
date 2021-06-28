from django import forms
from .models import *


class FormTipoespacoForm(forms.ModelForm):
    class Meta:
        model= Tipoespaco
        fields= ["descricao", "nome"]

class FormEnderecoForm(forms.ModelForm):
    class Meta:
        model= Enderecos
        fields= ["logradouro", "numero", "bairro", "cidade", "estado", "cep"]

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
    class Meta:
        model= Cliente
        fields= ["nome", "cpf_cnpj", "data_nascimento", "genero", "email", "telefone", "id_endereco"]

class FormFuncionariosForm(forms.ModelForm):
    class Meta:
        model= Funcionarios
        fields= ["nome", "cpf_cnpj", "data_nascimento", "genero", "email", "telefone", "id_endereco"]

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