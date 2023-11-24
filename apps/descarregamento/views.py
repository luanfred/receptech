from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import View
from datetime import datetime
from django.contrib.auth.decorators import login_required
from silo.models import Silo
from operador.models import Pessoa
from empresa.models import Empresa
from .models import Descarregamento
from django.http import JsonResponse
from django.db.models import Q
from django.db import models
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class Index(View):
    def get(self, request):
        filtro = request.GET.get('filtro')
        if filtro:
            descarregamentos = Descarregamento.objects.filter(
                Q(empresa_id__nome__icontains=filtro) |
                Q(nota_fiscal__icontains=filtro) |
                Q(placa__icontains=filtro) |
                Q(situacao__icontains=filtro) 
            )
        else:
            descarregamentos = Descarregamento.objects.all()
        paginator = Paginator(descarregamentos, 10)
        page = request.GET.get('page')
        descarregamentos = paginator.get_page(page)

        context = {
            'registros': descarregamentos,
            'qtd_leite_descarregado': self.qtd_leite_descarregado(),
            'total_veiculos_aguardando': self.total_veiculos_aguardando(),
            'filtro': filtro,
        }
        return render(request, 'login/home.html', context)
    
    def qtd_leite_descarregado(self):
        data_hoje = datetime.now().strftime('%Y-%m-%d')
        quantidade = Descarregamento.objects.filter(data=data_hoje, situacao='F').aggregate(models.Sum('qtd_litros_bomba'))
        if quantidade['qtd_litros_bomba__sum'] == None:
            return 0
        else:
            quantidade['qtd_litros_bomba__sum'] = locale.format_string('%d', quantidade['qtd_litros_bomba__sum'], grouping=True)
        return quantidade['qtd_litros_bomba__sum']
    
    def total_veiculos_aguardando(self):
        quantidade = Descarregamento.objects.exclude(situacao='F').count()
        return quantidade
        

class Editar(View):
    def get(self, request, id=None):
        if id:
            descarregamento = Descarregamento.objects.get(descarregamento_id=id)
            print(descarregamento.silo_id)
        else:
            descarregamento = None
        context = {
            'descarregamento': descarregamento,
            'silos': Silo.objects.all(),
            'data_hoje': datetime.now().strftime('%Y-%m-%d'),
        }
        return render(request, 'descarregamento/editar_descarregamento.html', context)

    def post(self, request):
        descarregamento_id = None if request.POST.get('descarregamento_id', '') == '' else request.POST.get('descarregamento_id', '')
        empresa_id = None if request.POST.get('empresa_empresa_id', '') == '' else request.POST.get('empresa_empresa_id', '')
        numero_nota_fiscal = None if request.POST.get('numero_nota_fiscal', '') == '' else request.POST.get('numero_nota_fiscal', '')
        placa = None if request.POST.get('placa', '') == '' else request.POST.get('placa', '')
        data = None if request.POST.get('data', '') == '' else request.POST.get('data', '')
        veiculo_esta_limpo = None if request.POST.get('veiculo_limpo', '') == '' else request.POST.get('veiculo_limpo', '')
        operadorcoleta_id = None if request.POST.get('codigo_operador_coleta', '') == '' else request.POST.get('codigo_operador_coleta', '')
        horario_coleta = None if request.POST.get('horario_coleta', '') == '' else request.POST.get('horario_coleta', '')
        primeiro_recipiente = None if request.POST.get('primeiro_recipiente', '') == '' else request.POST.get('primeiro_recipiente', '')
        segundo_recipiente = None if request.POST.get('segundo_recipiente', '') == '' else request.POST.get('segundo_recipiente', '')
        terceiro_recipiente = None if request.POST.get('terceiro_recipiente', '') == '' else request.POST.get('terceiro_recipiente', '')
        primeira_temperatura = None if request.POST.get('primeira_temperatura', '') == '' else request.POST.get('primeira_temperatura', '')
        segunda_temperatura = None if request.POST.get('segunda_temperatura', '') == '' else request.POST.get('segunda_temperatura', '')
        terceira_temperatura = None if request.POST.get('terceira_temperatura', '') == '' else request.POST.get('terceira_temperatura', '')
        quantidade_citrato = None if request.POST.get('qtd_citrato', '') == '' else request.POST.get('qtd_citrato', '')
        numero_lote_citrato = None if request.POST.get('numero_citrato', '') == '' else request.POST.get('numero_citrato', '')
        quantidade_fosfato = None if request.POST.get('qtd_fosfato', '') == '' else request.POST.get('qtd_fosfato', '')
        numero_lote_fosfato = None if request.POST.get('numero_fosfato', '') == '' else request.POST.get('numero_fosfato', '')
        operadoestabilizacao_id = None if request.POST.get('codigo_operador_estabilizar', '') == '' else request.POST.get('codigo_operador_estabilizar', '')
        horario_inicio_descarregamento = None if request.POST.get('descarregamento_horario_inicio', '') == '' else request.POST.get('descarregamento_horario_inicio', '')
        qtd_litros_nota = None if request.POST.get('qtd_litros_nota', '') == '' else request.POST.get('qtd_litros_nota', '')
        horario_termino_descarregamento = None if request.POST.get('descarregamento_horario_termino', '') == '' else request.POST.get('descarregamento_horario_termino', '')
        qtd_litros_contabilizado = None if request.POST.get('qtd_litros_bomba', '') == '' else request.POST.get('qtd_litros_bomba', '')
        diferenca = None if request.POST.get('diferenca', '') == '' else request.POST.get('diferenca', '')
        horario_saida_veiculo = None if request.POST.get('horario_saida_veiculo', '') == '' else request.POST.get('horario_saida_veiculo', '')
        silo_id = None if request.POST.get('silo_id', '') == '' else request.POST.get('silo_id', '')
        operadorlimpeza_id = None if request.POST.get('codigo_operador_limpeza', '') == '' else request.POST.get('codigo_operador_limpeza', '')
        
        situacao = self.verificar_situacao(
            horario_coleta,
            operadoestabilizacao_id,
            horario_inicio_descarregamento, 
            horario_termino_descarregamento
        )
        
        if operadorcoleta_id != None:
            operadorcoleta_id = Pessoa.objects.get(pessoa_id=operadorcoleta_id)
        if operadoestabilizacao_id != None:
            operadoestabilizacao_id = Pessoa.objects.get(pessoa_id=operadoestabilizacao_id)
        if operadorlimpeza_id != None:
            operadorlimpeza_id = Pessoa.objects.get(pessoa_id=operadorlimpeza_id)
        if empresa_id != None:
            empresa_id = Empresa.objects.get(empresa_id=empresa_id)
        if silo_id != None:
            silo_id = Silo.objects.get(silo_id=silo_id)
            
        if quantidade_citrato != None:
            quantidade_citrato = quantidade_citrato.replace(',', '.')
        if quantidade_fosfato != None:
            quantidade_fosfato = quantidade_fosfato.replace(',', '.')
        if qtd_litros_nota != None:
            qtd_litros_nota = qtd_litros_nota.replace('.', '')
        if qtd_litros_contabilizado != None:
            qtd_litros_contabilizado = qtd_litros_contabilizado.replace('.', '')
        if diferenca != None:
            diferenca = diferenca.replace('.', '')    
        
        descarregamento = Descarregamento(
            descarregamento_id = descarregamento_id,
            nota_fiscal = numero_nota_fiscal,
            placa = placa,
            data = data,
            veiculo_limpo =veiculo_esta_limpo ,
            qtd_citrato = quantidade_citrato,
            qtd_fosfato = quantidade_fosfato,
            lote_citrato = numero_lote_citrato,
            lote_fosfato = numero_lote_fosfato,
            horario_coleta = horario_coleta,
            horario_inicio_descarga = horario_inicio_descarregamento,
            horario_fim_descarga = horario_termino_descarregamento,
            horario_saida_veiculo = horario_saida_veiculo,
            qtd_litros_nota = qtd_litros_nota,
            qtd_litros_bomba = qtd_litros_contabilizado,
            diferenca = diferenca,
            situacao = situacao,
            primeiro_recipiente = primeiro_recipiente,
            segundo_recipiente = segundo_recipiente,
            terceiro_recipiente = terceiro_recipiente,
            temp_primeiro_recipiente = primeira_temperatura,
            temp_segundo_recipiente = segunda_temperatura,
            temp_terceiro_recipiente = terceira_temperatura,
            empresa_id = empresa_id,
            operadorcoleta_id =operadorcoleta_id,
            operadoestabilizacao_id = operadoestabilizacao_id,
            operadorlimpeza_id = operadorlimpeza_id,
            silo_id = silo_id,
        )
        descarregamento.save()
        
        return redirect('index_descarregamento')
    
    def verificar_situacao(
        self,
        horario_coleta,
        operadoestabilizacao_id,
        horario_inicio_descarregamento,
        horario_fim_descarregamento
        ):
    
        situacao = None
        if horario_coleta != None and operadoestabilizacao_id == None and horario_inicio_descarregamento == None and horario_fim_descarregamento == None:
            situacao = 'C'
        elif horario_coleta != None and operadoestabilizacao_id != None and horario_inicio_descarregamento == None and horario_fim_descarregamento == None:
            situacao = 'E'
        elif horario_coleta != None and operadoestabilizacao_id != None and horario_inicio_descarregamento != None and horario_fim_descarregamento == None:
            situacao = 'D'
        elif horario_coleta != None and operadoestabilizacao_id != None and horario_inicio_descarregamento != None and horario_fim_descarregamento != None:
            situacao = 'F'
        return situacao


@login_required()
def excluir_descarregamento(request, id):
    try:
        descarregamento = Descarregamento.objects.get(descarregamento_id=id)
        descarregamento.delete()
        context = {
            'status': 'ok',
            'msg': 'descarregamento excluído com sucesso!'
        }
    except:
        context = {
            'status': 'erro',
            'msg': 'Erro ao excluir descarregamento!'
        }
    return JsonResponse(context)
