from distutils import core
from django import urls
from django.urls import path
from .views import *
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name='index'),
    path('login_ingresar',login_ingresar,name='login_ingresar'),
    path('usuariopreferencia/',login_required(UsuarioPreferenciaListView.as_view()), name = 'usuariopreferencia_list')
] 


