
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_usuario/', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
