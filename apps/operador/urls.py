from django.urls import path
from .views import Index, Editar, excluir_operador, listar_operadores, buscar_operador
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Index.as_view()), name='index_operador'),
    path('cadastrar/', login_required(Editar.as_view()), name='cadastrar_operador'),
    path('editar/<int:id>/', login_required(Editar.as_view()), name='editar_operador'),
    path('excluir/<int:id>/', excluir_operador, name='excluir_operador'),
    path('listar/', listar_operadores, name='listar_operador'),
    path('buscar/<int:id>', buscar_operador, name='buscar_operador')
]