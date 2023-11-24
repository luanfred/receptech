from django.db import models

class Silo(models.Model):
    silo_id = models.AutoField(primary_key=True)
    quantidade = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'silo'
        db_table = 'silos'