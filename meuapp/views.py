from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'meuapp/home.html')

@login_required(login_url='login')
def crudCurso(request):
    cursos = Curso.objects.all().order_by('nome')
    conteudo = {"cursos": cursos}

    return render(request, 'meuapp/cursos/crud.html', conteudo)    

@login_required(login_url='login')
def createCurso(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("curso.crud") 

    conteudo = {"form": form}
    return render(request, 'meuapp/cursos/criar.html', conteudo) 


def listagemCurso(request):
    cursos = Curso.objects.all().order_by('nome')
    conteudo = {"cursos": cursos}

    return render(request, 'meuapp/cursos/listagem.html', conteudo) 

@login_required(login_url='login')
def updateCurso(request, id):
    curso = Curso.objects.get(pk=id)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect("curso.crud") 

    conteudo = {"form": form, "curso": curso}
    return render(request, 'meuapp/cursos/editar.html', conteudo)

@login_required(login_url='login')
def deleteCurso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect("curso.crud") 

def consulta(request):
    if request.method == 'GET':    
        txtPesquisa = request.GET.get('txtPesquisa')
        if txtPesquisa is None: 
            txtPesquisa = ''
        cursos = Curso.objects.filter(nome__icontains=txtPesquisa).order_by('nome')
        
        return render(request, "meuapp/consulta.html", { 'cursos': cursos, 'txtPesquisa': txtPesquisa })

def sobre(request):
    return render(request, 'meuapp/sobre.html')