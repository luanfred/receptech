# Generated by Django 4.2.4 on 2023-09-27 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silo', '0002_remove_silo_descricao_silo_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='silo',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
