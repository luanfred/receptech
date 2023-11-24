from django.db import models

class Empresa(models.Model):
    empresa_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    cpfcnpj = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        app_label = 'empresa'
        db_table = 'empresas'
