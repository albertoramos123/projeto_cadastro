
from django.contrib import admin
from django.urls import path
from app_cadastro import views

urlpatterns = [
    #rota, view responsável, nome de referencia
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
