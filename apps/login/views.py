from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

class loginView(View):
    def get(self, request):
        return render(request, 'login/login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        username = User.objects.filter(username=email).first()
        if username is None:
            messages.error(request, 'Usuário não cadastrado! Faça seu cadastro')
            return redirect('login')
        
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('index_descarregamento')  
        else:
            messages.error(request, 'Email ou senha incorretos')
            return redirect('login')

