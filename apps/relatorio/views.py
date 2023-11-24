from django.shortcuts import render, redirect
from django.views.generic import View
import pdfkit
from django.http import HttpResponse
from pathlib import Path
import os
from .config import env, confing
from silo.models import Silo
from django.db.models import Q
from django.contrib import messages
from descarregamento.models import Descarregamento
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from setup.settings import EMAIL_HOST_USER
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Relatorio(View):
    def get(self, request):
        context = {
            'silos': Silo.objects.all(),
        }
        return render(request, 'relatorio/tela_filtros.html', context=context)

    def post(self, request):
        template = env.get_template('relatorio_recebimento.html')
        context = self.buscar_descarregamentos(request)
        template = template.render(context)
        pdf = pdfkit.from_string(template, False, confing)

        email = request.POST.get('email_form')
        if email not in (None, ''):
            email_mensagem = EmailMessage(
                'Relatório de Descarregamentos',
                'Segue em anexo o relatório de descarregamentos',
                EMAIL_HOST_USER,
                [email],
            )
            email_mensagem.attach('relatorio_descarregamento.pdf', pdf, 'application/pdf')
            email_mensagem.send()
            messages.success(request, 'Email enviado com sucesso!')
            return redirect('tela_filtros_relatorio')   
        else:
            response = HttpResponse(
                pdf,
                headers={
                    'Content-Type': 'application/pdf',
                    'Content-Disposition': 'attachment; filename="relatorio_descarregamento.pdf"',
                }
            )
            return response

    def buscar_descarregamentos(self, request):
        operadorcoleta_id = None if request.POST.get('codigo_operador_coleta') == '' else request.POST.get('codigo_operador_coleta')
        operadoestabilizacao_id = None if request.POST.get('codigo_operador_estabilizar') == '' else request.POST.get('codigo_operador_estabilizar')
        operadorlimpeza_id = None if request.POST.get('codigo_operador_limpeza') == '' else request.POST.get('codigo_operador_limpeza')
        emrpresa_id = None if request.POST.get('empresa_empresa_id') == '' else request.POST.get('empresa_empresa_id')
        lote_citrato = None if request.POST.get('numero_citrato') == '' else request.POST.get('numero_citrato')
        lote_fosfato = None if request.POST.get('numero_fosfato') == '' else request.POST.get('numero_fosfato')
        placa = None if request.POST.get('placa') == '' else request.POST.get('placa')
        nota_fiscal = None if request.POST.get('nota_fiscal') == '' else request.POST.get('nota_fiscal')
        silo_id = None if request.POST.get('silo_id') == '' else request.POST.get('silo_id')
        data_inicial = None if request.POST.get('data_inicio') == '' else request.POST.get('data_inicio')
        data_final = None if request.POST.get('data_final') == '' else request.POST.get('data_final')
        ordenar = None if request.POST.get('ordenar') == '' else request.POST.get('ordenar')
        
        descarregamentos = None
        filtros = Q()
        
        if operadorcoleta_id:
            filtros &= Q(operadorcoleta_id=operadorcoleta_id)
        if operadoestabilizacao_id:
            filtros &= Q(operadoestabilizacao_id=operadoestabilizacao_id)
        if operadorlimpeza_id:
            filtros &= Q(operadorlimpeza_id=operadorlimpeza_id)
        if emrpresa_id:
            filtros &= Q(empresa_id=emrpresa_id)
        if lote_citrato:
            filtros &= Q(lote_citrato__icontains=lote_citrato)
        if lote_fosfato:
            filtros &= Q(lote_fosfato__icontains=lote_fosfato)
        if placa:
            filtros &= Q(placa__icontains=placa)
        if nota_fiscal:
            filtros &= Q(nota_fiscal=nota_fiscal)
        if silo_id:
            filtros &= Q(silo_id=silo_id)
        if data_inicial:
            filtros &= Q(data__gte=data_inicial)
        if data_final:
            filtros &= Q(data__lte=data_final)
        
        if filtros:
            descarregamentos = Descarregamento.objects.filter(filtros).order_by(ordenar)
        else:
            descarregamentos = Descarregamento.objects.all().order_by(ordenar)
                    
        for i in descarregamentos:
            i.data = i.data.strftime('%d/%m/%Y')
            
            if i.horario_coleta:
                i.horario_coleta = i.horario_coleta.strftime('%H:%M')
            if i.horario_inicio_descarga:
                i.horario_inicio_descarga = i.horario_inicio_descarga.strftime('%H:%M')
            if i.horario_fim_descarga:
                i.horario_fim_descarga = i.horario_fim_descarga.strftime('%H:%M')
            if i.horario_saida_veiculo:
                i.horario_saida_veiculo = i.horario_saida_veiculo.strftime('%H:%M')
                
            if i.situacao == 'C':
                i.situacao = 'Coletado'
            elif i.situacao == 'E':
                i.situacao = 'Estabilizado'
            elif i.situacao == 'D':
                i.situacao = 'Descarregando'
            elif i.situacao == 'F':
                i.situacao = 'Finalizado'   
                
            if i.veiculo_limpo:
                i.veiculo_limpo = 'Sim'
            else:
                i.veiculo_limpo = 'Não'
            
            if i.qtd_citrato:
                i.qtd_citrato = str(i.qtd_citrato).replace('.', ',')
            if i.qtd_fosfato:
                i.qtd_fosfato = str(i.qtd_fosfato).replace('.', ',')
            if i.qtd_litros_nota:
                i.qtd_litros_nota = locale.format_string('%d', i.qtd_litros_nota, grouping=True)
            if i.qtd_litros_bomba:
                i.qtd_litros_bomba = locale.format_string('%d', i.qtd_litros_bomba, grouping=True)
            if i.diferenca:
                i.diferenca = locale.format_string('%d', i.diferenca, grouping=True)
              
        context = {
            'descarregamentos': descarregamentos,
        }
        return context
        
        
            
        
