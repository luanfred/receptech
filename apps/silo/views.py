from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import View
from datetime import datetime
from .models import Silo
from django.http import JsonResponse
from django.db.models import Q
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
            query = gerar_query_busca(Silo, filtro)
            silo = Silo.objects.filter(query)
        else:
            silo = Silo.objects.all()
        paginator = Paginator(silo, 10)
        page = request.GET.get('page')
        silo = paginator.get_page(page)

        context = {
            'registros': silo,
            'filtro': filtro,
        }
        return render(request, 'silo/listar_silo.html', context)


class Editar(View):
    def get(self, request, id=None):
        if id:
            silo = Silo.objects.get(silo_id=id)
        else:
            silo = None
        context = {
            'silo': silo,
        }
        return render(request, 'silo/editar_silo.html', context)

    def post(self, request):
        codigo = request.POST.get('codigo_silo')
        quantidade = request.POST.get('quantidade')

        if codigo == '':
            codigo = None

        silo = Silo(
            silo_id=codigo,
            quantidade=quantidade,
        )
        silo.save()

        return redirect('index_silo')
    

@login_required()
def excluir_silo(request, id):
    try:
        silo = Silo.objects.get(silo_id=id)
        silo.delete()
        context = {
            'status': 'ok',
            'msg': 'Silo excluído com sucesso!'
        }
    except:
        context = {
            'status': 'erro',
            'msg': 'Erro ao excluir Silo!'
        }
    return JsonResponse(context)


@login_required()
def listar_silo(request):
    silos = Silo.objects.values('silo_id', 'quantidade')
    return JsonResponse(list(silos), safe=False)
