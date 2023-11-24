from django.db import models

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpfcnpj = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)

    class Meta:
        db_table = 'usuarios'
