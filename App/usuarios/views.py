from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from home.views import home
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth

@has_permission_decorator('cadastrar_usuario')
def cadastrar_usuario(request):
    if request.method == "GET":
        return render(request, 'usuarios.html')
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar messages do Danjo 
            return HttpResponse('Email já existe!')
        
        user = Users.objects.create_user(username=email, email=email, password=senha, cargo="E" )

        # TODO: Redirecionar com uma mensagem.
        return HttpResponse('Conta criada')
    
def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('login'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            # TODO: Redirecionar com mensagem de erro
            return HttpResponse('Usuario inválido')
        
        auth.login(request, user)
        # return HttpResponse('Usuário logado com sucesso!')
        return render(request, 'home.html')
    
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))