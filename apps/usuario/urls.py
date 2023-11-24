from django.urls import path
from .views import CadastroView

urlpatterns = [
    path('cadastro', CadastroView.as_view(), name='cadastrar_usuario'),
]