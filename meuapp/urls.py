"""sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('cursos/crud', views.crudCurso, name='curso.crud'),
    path('cursos/', views.listagemCurso, name='curso.read'),
    path('curso/c/', views.createCurso, name='curso.create'),
    path('curso/e/<int:id>', views.updateCurso, name='curso.update'),
    path('curso/d/<int:id>', views.deleteCurso, name='curso.delete'),
    path('consulta/', views.consulta, name='consulta'),
    path('sobre/', views.sobre, name='sobre'),
]
