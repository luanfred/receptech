# Generated by Django 4.2.4 on 2023-10-18 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descarregamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='descarregamento',
            name='diferenca',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
