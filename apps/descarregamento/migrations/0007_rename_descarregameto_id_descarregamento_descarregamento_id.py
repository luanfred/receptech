# Generated by Django 4.2.4 on 2023-10-21 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('descarregamento', '0006_rename_horatio_saida_veiculo_descarregamento_horario_saida_veiculo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='descarregamento',
            old_name='descarregameto_id',
            new_name='descarregamento_id',
        ),
    ]
