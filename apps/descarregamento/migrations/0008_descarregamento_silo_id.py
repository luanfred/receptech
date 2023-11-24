# Generated by Django 4.2.4 on 2023-10-21 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silo', '0003_alter_silo_quantidade'),
        ('descarregamento', '0007_rename_descarregameto_id_descarregamento_descarregamento_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='descarregamento',
            name='silo_id',
            field=models.ForeignKey(blank=True, db_column='silo_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='silo.silo'),
        ),
    ]
