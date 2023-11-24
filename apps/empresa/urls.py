from django.urls import path
from .views import Index, Editar, excluir_empresa, listar_empresa, buscar_empresa
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Index.as_view()), name='index_empresa'),
    path('cadastrar/', login_required(Editar.as_view()), name='cadastrar_empresa'),
    path('editar/<int:id>/', login_required(Editar.as_view()), name='editar_empresa'),
    path('excluir/<int:id>/', excluir_empresa, name='excluir_empresa'),
    path('listar/', listar_empresa, name='listar_empresa'),
    path('buscar/<int:id>', buscar_empresa, name='buscar_empresa')
]
