from django.shortcuts import render
from django.shortcuts import render, redirect
#from .form import *

# Create your views here.
def home(request):
    return render(request, 'meuapp/home.html')

def createCurso(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/listagemCurso")  # mudar

    conteudo = {"formulario": form}
    return render(request, 'meuapp/cursos/criar.html', conteudo) #mudar


def listagemCurso(request):
    curso = Curso.objects.all().order_by('nome')
    conteudo = {"curso": curso}

    return render(request, 'meuapp/cursos/listagem.html', conteudo) #mudar


def crud(request):
     return render(request, 'meuapp/cursos/crud.html')    


def updateCurso(request, id):
    curso = Curso.objects.get(pk=id)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect("/listagemCurso")  # mudar

    conteudo = {"formulario": form}
    return render(request, 'meuapp/cursos/criar.html', conteudo)


def deleteCurso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect("/listagemCurso") #mudar

def consulta(request):
    return render(request, 'meuapp/consulta.html')


def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')

    results = Curso.objects.filter(nome__icontains=query)
    return render(request, "search.html", {'query': query, 'results': results})

def sobre(request):
    return render(request, 'meuapp/sobre.html')