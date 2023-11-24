from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import View
from datetime import datetime
from .models import Pessoa
from django.http import JsonResponse
from django.db.models import Q
from django.core import serializers
from django.contrib.auth.decorators import login_required

def gerar_query_busca(model, filtro):
    query = Q()
    for campo in model._meta.fields:
        nome_campo = campo.name
        query |= Q(**{nome_campo + '__icontains': filtro})
    return query


class Index(View):
    def get(self, request):
        filtro = request.GET.get('filtro')
        if filtro:
            query = gerar_query_busca(Pessoa, filtro)
            operadores = Pessoa.objects.filter(query)
        else:
            operadores = Pessoa.objects.all()
        paginator = Paginator(operadores, 10)
        page = request.GET.get('page')
        operadores = paginator.get_page(page)

        context = {
            'registros': operadores,
            'filtro': filtro,
        }
        return render(request, 'operador/listar_operador.html', context)


class Editar(View):
    def get(self, request, id=None):
        if id:
            operador = Pessoa.objects.get(pessoa_id=id)
        else:
            operador = None
        context = {
            'operador': operador,
            'data_hoje': datetime.now().strftime('%Y-%m-%d'),
        }
        return render(request, 'operador/editar_operador.html', context)

    def post(self, request, id=None):
        codigo = request.POST.get('codigo_operador')
        nome = request.POST.get('nome_operador')
        data_cadastro = request.POST.get('data_cadastro_operador')
        turno = request.POST.get('turno_operador')

        if codigo == '':
            codigo = None
        nome = nome.strip()

        pessoa = Pessoa(
            pessoa_id=codigo,
            nome=nome,
            datacadastro=data_cadastro,
            turno=turno
        )
        pessoa.save()

        return redirect('index_operador')


@login_required()
def excluir_operador(request, id):
    try:
        operador = Pessoa.objects.get(pessoa_id=id)
        operador.delete()
        context = {
            'status': 'ok',
            'msg': 'Operador excluído com sucesso!'
        }
    except:
        context = {
            'status': 'erro',
            'msg': 'Erro ao excluir operador!'
        }
    return JsonResponse(context)


@login_required()
def listar_operadores(request):
    operadores = Pessoa.objects.values('pessoa_id', 'nome', 'turno')
    paginator = Paginator(operadores, 10)
    page = request.GET.get('page')
    operadores_paginados = paginator.get_page(page)
    operadores = list(operadores_paginados)
    context = {
        'registros': operadores,
        'registro_inicial': operadores_paginados.start_index(),
        'registro_final': operadores_paginados.end_index(),
        'total_registros': operadores_paginados.paginator.count,
        'tem_pagina_anterior': operadores_paginados.has_previous(),
        'pagina_anterior': operadores_paginados.previous_page_number() if operadores_paginados.has_previous() else None,
        'tem_proxima_pagina': operadores_paginados.has_next(),
        'proxima_pagina': operadores_paginados.next_page_number() if operadores_paginados.has_next() else None,
    }
    
    return JsonResponse(context, safe=False)


@login_required()
def buscar_operador(request, id):
    try:
        operadores = Pessoa.objects.get(pessoa_id=id)
        context = {
            'status': 'ok',
            'pessoa_id': operadores.pessoa_id,
            'nome': operadores.nome,
            'datacadastro': operadores.datacadastro,
            'turno': operadores.turno,
        }
    except:
        context = {
            'status': 'erro',
            'mensagem': 'Operador não encontrado!'
        }
    return JsonResponse(context)