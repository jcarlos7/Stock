from django.shortcuts import render
from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator
from .models import Users

@has_permission_decorator('cadastrar_usuario')
def cadastrar_usuario(request):
    if request.method == "GET":
        return render(request, 'usuarios.html')
    if request.method == "POST"
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar messages do Danjo 
            return HttpResponse('Email já existe!')
