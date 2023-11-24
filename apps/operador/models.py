from django.db import models

class Pessoa(models.Model):
    pessoa_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    turno = models.CharField(max_length=1, blank=True, null=True)
    datacadastro = models.DateField(null=True, blank=True)

    class Meta:
        app_label = 'operador'
        db_table = 'pessoas'
