from django.urls import path
from .views import Index, Editar, excluir_silo, listar_silo
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Index.as_view()), name='index_silo'),
    path('cadastrar/', login_required(Editar.as_view()), name='cadastrar_silo'),
    path('editar/<int:id>/', login_required(Editar.as_view()), name='editar_silo'),
    path('excluir/<int:id>/', excluir_silo, name='excluir_silo'),
    path('listar/', listar_silo, name='listar_silo')
]