from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Usuario
from django.contrib import messages

class CadastroView(View):

    def get(self, request):
        return render(request, 'usuario/cadastrar_usuario.html')

    def post(self, request):

        nome = request.POST.get('nome').strip()
        cpfcnpj = request.POST.get('cpfcnpj').strip()
        telefone = request.POST.get('telefone').strip()
        email = request.POST.get('email').strip()
        senha = request.POST.get('senha').strip()
        confirmacao_senha = request.POST.get('confirmacao_senha').strip()
        valido = True

        if senha != confirmacao_senha:
            messages.error(request, 'Senhas não conferem')
            valido = False

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email já cadastrado')
            valido = False

        if not valido:
            return redirect('cadastrar_usuario')

        User.objects.create_user(username=email, password=senha)
        Usuario.objects.create(
            nome=nome,
            cpfcnpj=cpfcnpj,
            telefone=telefone,
            email=email,
        )
        return redirect('login')
