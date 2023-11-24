# Generated by Django 4.2.4 on 2023-09-26 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('empresa_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('cpfcnjp', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
                ('cep', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'empresas',
            },
        ),
    ]