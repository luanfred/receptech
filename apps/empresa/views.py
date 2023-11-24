from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import View
from datetime import datetime
from .models import Empresa
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
            query = gerar_query_busca(Empresa, filtro)
            empresa = Empresa.objects.filter(query)
        else:
            empresa = Empresa.objects.all()
        paginator = Paginator(empresa, 10)
        page = request.GET.get('page')
        empresa = paginator.get_page(page)

        context = {
            'registros': empresa,
            'filtro': filtro,
        }
        return render(request, 'empresa/listar_empresa.html', context)


class Editar(View):
    def get(self, request, id=None):
        if id:
            empresa = Empresa.objects.get(empresa_id=id)
        else:
            empresa = None
        context = {
            'empresa': empresa,
            'data_hoje': datetime.now().strftime('%Y-%m-%d'),
        }
        return render(request, 'empresa/editar_empresa.html', context)

    def post(self, request):
        codigo = request.POST.get('codigo_empresa')
        razao_social = request.POST.get('razao_social').strip()
        cpfcnpj = request.POST.get('cpfcnpj').strip()
        telefone = request.POST.get('telefone').strip()
        cep = request.POST.get('cep').strip()
        endereco = request.POST.get('endereco').strip()
        numero = request.POST.get('numero').strip()
        bairro = request.POST.get('bairro').strip()
        cidade = request.POST.get('cidade').strip()
        uf = request.POST.get('uf').strip()

        if codigo == '':
            codigo = None

        empresa = Empresa(
            empresa_id=codigo,
            nome=razao_social,
            cpfcnpj=cpfcnpj,
            telefone=telefone,
            endereco=endereco,
            numero=numero,
            bairro=bairro,
            cidade=cidade,
            uf=uf,
            cep=cep,
        )
        empresa.save()

        return redirect('index_empresa')


@login_required()
def excluir_empresa(request, id):
    try:
        empresa = Empresa.objects.get(empresa_id=id)
        empresa.delete()
        context = {
            'status': 'ok',
            'msg': 'Empresa excluído com sucesso!'
        }
    except:
        context = {
            'status': 'erro',
            'msg': 'Erro ao excluir empresa!'
        }
    return JsonResponse(context)


@login_required()
def listar_empresa(request):
    empresas = Empresa.objects.values('empresa_id', 'nome', 'cpfcnpj')
    paginator = Paginator(empresas, 10)
    page = request.GET.get('page')
    empresas_paginados = paginator.get_page(page)
    empresas = list(empresas_paginados)
    context = {
        'registros': empresas,
        'registro_inicial': empresas_paginados.start_index(),
        'registro_final': empresas_paginados.end_index(),
        'total_registros': empresas_paginados.paginator.count,
        'tem_pagina_anterior': empresas_paginados.has_previous(),
        'pagina_anterior': empresas_paginados.previous_page_number() if empresas_paginados.has_previous() else None,
        'tem_proxima_pagina': empresas_paginados.has_next(),
        'proxima_pagina': empresas_paginados.next_page_number() if empresas_paginados.has_next() else None,
    }
    
    return JsonResponse(context, safe=False)


@login_required()
def buscar_empresa(request, id):
    try:
        empresas = Empresa.objects.get(empresa_id=id)
        context = {
            'status': 'ok',
            'empresa_id': empresas.empresa_id,
            'nome': empresas.nome,
            'cpfcnpj': empresas.cpfcnpj,
        }
    except:
        context = {
            'status': 'erro',
            'mensagem': 'Empresa não encontrada!'
        }
    return JsonResponse(context)

