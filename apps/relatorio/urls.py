from django.urls import path
from .views import Relatorio
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Relatorio.as_view()), name='tela_filtros_relatorio'),
    path('recebimentos/', login_required(Relatorio.as_view()), name='gerar_relatorio_recebimentos'),
]
