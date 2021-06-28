# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#Validação: ok
class Tipoespaco(models.Model):
    id_tipoespaco = models.AutoField(db_column='id_tipoEspaco', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=200, blank=True, null=True)
    nome = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipoEspaco'

#Validação: ok
class Enderecos(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=45)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=35)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'enderecos'

#Validação: ok
class Pagamento(models.Model):
    id_pagamento = models.AutoField(primary_key=True)
    metodo = models.CharField(max_length=45)
    cod_mercadopago = models.IntegerField()
    aprovado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pagamento'

#Validação: ok
class Espacos(models.Model):
    id_espaco = models.AutoField(primary_key=True)
    id_tipo_espaco = models.ForeignKey('Tipoespaco', models.DO_NOTHING, db_column='id_tipo_espaco')
    preco = models.FloatField()

    class Meta:
        managed = False
        db_table = 'espacos'


#Validação: ok
class Equipamentos(models.Model):
    id_equipamento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    descrição = models.CharField(max_length=100)
    preco = models.FloatField()

    class Meta:
        managed = False
        db_table = 'equipamentos'


#Validação: ok
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    cpf_cnpj = models.CharField(max_length=14)
    data_nascimento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=2, blank=True, null=True)
    email = models.CharField(max_length=40)
    telefone = models.CharField(max_length=20)
    id_endereco = models.ForeignKey('Enderecos', models.DO_NOTHING, db_column='id_endereco')

    class Meta:
        managed = False
        db_table = 'cliente'

#Validação: ok
class Funcionarios(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    cpf_cnpj = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=2, blank=True, null=True)
    email = models.CharField(max_length=40)
    telefone = models.CharField(max_length=20)
    id_endereco = models.ForeignKey(Enderecos, models.DO_NOTHING, db_column='id_endereco')

    class Meta:
        managed = False
        db_table = 'funcionarios'

#Validação: ok
class Pacotehoras(models.Model):
    id_pacote_horas = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', related_name='pacote_id_cliente')
    qtd_horas = models.IntegerField()
    id_empresa = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True, related_name='pacote_id_empresa')

    class Meta:
        managed = False
        db_table = 'pacoteHoras'

#Validação: ok
class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_pagamento = models.ForeignKey(Pagamento, models.DO_NOTHING, db_column='id_pagamento', blank=True, null=True)
    data_log = models.DateField()
    hora_log = models.TimeField()
    id_espaco = models.ForeignKey(Espacos, models.DO_NOTHING, db_column='id_espaco')
    id_pacote_horas = models.ForeignKey(Pacotehoras, models.DO_NOTHING, db_column='id_pacote_horas', blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    data_reserva = models.DateField()
    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()
    hora_limpeza = models.TimeField()

    class Meta:
        managed = False
        db_table = 'reserva'

#Validação: ok
class Advertencias(models.Model):
    id_advertencias = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=500)
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva')
    id_funcionario = models.ForeignKey('Funcionarios', models.DO_NOTHING, db_column='id_funcionario')

    class Meta:
        managed = False
        db_table = 'advertencias'

#Validação: ok
class Convidados(models.Model):
    id_convidado = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convidados'


#Validação: ok
class Equipamentoreserva(models.Model):
    id_reserva = models.OneToOneField('Reserva', models.DO_NOTHING, db_column='id_reserva', primary_key=True)
    id_equipamento = models.ForeignKey('Equipamentos', models.DO_NOTHING, db_column='id_equipamento')

    class Meta:
        managed = False
        db_table = 'equipamentoReserva'
        unique_together = (('id_reserva', 'id_equipamento'),)


