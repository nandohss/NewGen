# Generated by Django 3.2.4 on 2021-06-29 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertencias',
            fields=[
                ('id_advertencias', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'advertencias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
                ('cpf_cnpj', models.CharField(max_length=14)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, max_length=2, null=True)),
                ('email', models.CharField(max_length=40)),
                ('telefone', models.CharField(max_length=20)),
                ('logradouro', models.CharField(max_length=45)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=35)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Convidados',
            fields=[
                ('id_convidado', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'convidados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipamentos',
            fields=[
                ('id_equipamento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20)),
                ('descrição', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
            ],
            options={
                'db_table': 'equipamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Espacos',
            fields=[
                ('id_espaco', models.AutoField(primary_key=True, serialize=False)),
                ('preco', models.FloatField()),
            ],
            options={
                'db_table': 'espacos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id_funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
                ('cpf_cnpj', models.CharField(max_length=14)),
                ('data_nascimento', models.DateField()),
                ('genero', models.CharField(blank=True, max_length=2, null=True)),
                ('email', models.CharField(max_length=40)),
                ('telefone', models.CharField(max_length=20)),
                ('logradouro', models.CharField(max_length=45)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=35)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'funcionarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pacotehoras',
            fields=[
                ('id_pacote_horas', models.AutoField(primary_key=True, serialize=False)),
                ('qtd_horas', models.IntegerField()),
            ],
            options={
                'db_table': 'pacoteHoras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id_pagamento', models.AutoField(primary_key=True, serialize=False)),
                ('metodo', models.CharField(max_length=45)),
                ('cod_mercadopago', models.IntegerField()),
                ('aprovado', models.IntegerField()),
            ],
            options={
                'db_table': 'pagamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('data_log', models.DateField()),
                ('hora_log', models.TimeField()),
                ('id_empresa', models.IntegerField(blank=True, null=True)),
                ('data_reserva', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('hora_saida', models.TimeField()),
                ('hora_limpeza', models.TimeField()),
            ],
            options={
                'db_table': 'reserva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipoespaco',
            fields=[
                ('id_tipoespaco', models.AutoField(db_column='id_tipoEspaco', primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, max_length=200, null=True)),
                ('nome', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tipoEspaco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipamentoreserva',
            fields=[
                ('id_reserva', models.OneToOneField(db_column='id_reserva', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='newgenapp.reserva')),
            ],
            options={
                'db_table': 'equipamentoReserva',
                'managed': False,
            },
        ),
    ]