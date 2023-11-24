from operador.models import Pessoa
from django.db import models
from empresa.models import Empresa
from silo.models import Silo

class Descarregamento(models.Model):
    descarregamento_id = models.AutoField(primary_key=True)
    nota_fiscal = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=15, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    veiculo_limpo = models.CharField(max_length=1, blank=True, null=True)
    qtd_citrato = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    qtd_fosfato = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    lote_citrato = models.CharField(max_length=50, blank=True, null=True)
    lote_fosfato = models.CharField(max_length=50, blank=True, null=True)
    horario_coleta = models.TimeField(null=True, blank=True)
    horario_inicio_descarga = models.TimeField(blank=True, null=True)
    horario_fim_descarga = models.TimeField(blank=True, null=True)
    horario_saida_veiculo = models.TimeField(null=True, blank=True)
    qtd_litros_nota = models.IntegerField(blank=True, null=True)
    qtd_litros_bomba = models.IntegerField(blank=True, null=True)
    diferenca = models.IntegerField(blank=True, null=True)
    situacao = models.CharField(max_length=1, blank=True, null=True)
    primeiro_recipiente = models.IntegerField(null=True, blank=True)
    segundo_recipiente = models.IntegerField(null=True, blank=True)
    terceiro_recipiente = models.IntegerField(null=True, blank=True)
    temp_primeiro_recipiente = models.IntegerField(null=True, blank=True)
    temp_segundo_recipiente = models.IntegerField(null=True, blank=True)
    temp_terceiro_recipiente = models.IntegerField(null=True, blank=True)

    empresa_id = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa_id', blank=True, null=True)
    operadorcoleta_id = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='operadorcoleta_id', blank=True, null=True, related_name='operadorcoleta_id')
    operadoestabilizacao_id = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='operadoestabilizacao_id', blank=True, null=True)
    operadorlimpeza_id = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='operadorlimpeza_id', blank=True, null=True, related_name='operadorlimpeza_id')
    silo_id = models.ForeignKey(Silo, models.DO_NOTHING, db_column='silo_id', blank=True, null=True)

    class Meta:
        app_label = 'descarregamento'
        db_table = 'descarregamentos'
        
"""
    C - Coletado
    E - Estabilizado
    D - Descarregando
    F - Finalizado
"""
 
"""
empresa_id =  ok
placa = ok
nota_fiscal = ok
data = ok
veiculo_limpo = ok
situacao = 

operadorcoleta_id = 
primeiro_recipiente = 
segundo_recipiente = 
terceiro_recipiente = 
horario_coleta = 
temp_primeiro_recipiente = 
temp_segundo_recipiente = 
temp_terceiro_recipiente = 

operadoestabilizacao_id = 
qtd_citrato = 
qtd_fosfato = 
lote_citrato = 
lote_fosfato = 

operadorlimpeza_id = 
horario_inicio_descarga = 
horario_fim_descarga = 
horario_saida_veiculo = 
qtd_litros_nota = 
qtd_litros_bomba = 
diferenca = 
silo_id =

"""