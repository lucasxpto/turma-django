# Generated by Django 4.2.4 on 2023-08-09 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=70, verbose_name='Sobrenome')),
                ('endereco', models.CharField(max_length=100, verbose_name='endereco')),
                ('data_nascimento', models.DateTimeField(verbose_name='Data de nascimento')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('turno', models.CharField(choices=[('matutino', 'Matutino'), ('vespertino', 'Vespertino'), ('noturno', 'Noturno')], max_length=10, verbose_name='Turno')),
            ],
        ),
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.PositiveIntegerField(verbose_name='Período')),
                ('aluno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.aluno')),
            ],
            options={
                'verbose_name': 'Boletim',
                'verbose_name_plural': 'Boletins',
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos_turma', to='core.turma'),
        ),
    ]
