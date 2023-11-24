from django.urls import path
from .views import Editar, excluir_descarregamento, Index
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Index.as_view()), name='index_descarregamento'),
    path('cadastrar', login_required(Editar.as_view()), name='cadastrar_descarregamento'),
    path('editar/<int:id>', login_required(Editar.as_view()), name='editar_descarregamento'),
    path('excluir/<int:id>/', excluir_descarregamento, name='excluir_descarregamento')
]