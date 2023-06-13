from django.shortcuts import render
from rest_framework import viewsets

from .models import Texte, Livre, Titre, Chapitre, Section, Article, Alinea
from .serializers import TexteSerializer, LivreSerializer, TitreSerializer, ChapitreSerializer, SectionSerializer, ArticleSerializer, AlineaSerializer

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
import requests

# Create your views here.

class Home(ListView):

    model = Texte
    template_name = 'home.html'
    context_object_name = 'textes'

class TexteViewSet(viewsets.ModelViewSet):
    
    queryset = Texte.objects.all()
    serializer_class = TexteSerializer
    filterset_fields = ['id']

class LivreViewSet(viewsets.ModelViewSet):
    
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    filterset_fields = ['text', 'numero']

class TitreViewSet(viewsets.ModelViewSet):
    
    queryset = Titre.objects.all()
    serializer_class = TitreSerializer
    filterset_fields = ['livre', 'numero']

class ChapitreViewSet(viewsets.ModelViewSet):
    
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreSerializer
    filterset_fields = ['titre', 'numero']

class SectionViewSet(viewsets.ModelViewSet):
    
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filterset_fields = ['chapitre', 'numero']

class ArticleViewSet(viewsets.ModelViewSet):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['section', 'numero']

class AlineaViewSet(viewsets.ModelViewSet):
    
    queryset = Alinea.objects.all()
    serializer_class = AlineaSerializer
    filterset_fields = ['article', 'numero']

def livres_cpp_view(request):
    response = requests.get('http://127.0.0.1:8000/api/livres/?text=2&numero=')
    if response.status_code == 200:
        data = response.json()
        context = {'data' : data}
        return render(request, 'livrescpp.html', context)
    else:
        return render(request, 'error.html')

#def titres_cpp_view(request):
    #response = requests.get('http://127.0.0.1:8000/titres/?livre=1&numero=')
#    if response.status_code == 200:
#        data = response.json()
#        context = {'data' : data}
#        return render(request, 'titrescpp.html', context)
#    else:
#        return render(request, 'error.html')

def titres_cpp_view(request):
    TitreResponse = requests.get('http://127.0.0.1:8000/api/titres/?livre=1&numero=')
    chapResponse = requests.get('http://127.0.0.1:8000/api/chapitres/')
    secResponse = requests.get('http://127.0.0.1:8000/api/sections/')
    articleResponse = requests.get('http://127.0.0.1:8000/api/articles/')
    alineaResponse = requests.get('http://127.0.0.1:8000/api/alineas/')
    if TitreResponse.status_code == 200 and chapResponse.status_code == 200:
        data = TitreResponse.json()
        chapters = chapResponse.json()
        sections = secResponse.json()
        articles = articleResponse.json()
        alineas = alineaResponse.json()
        context = {'data': data, 'chapters': chapters, 'sections': sections, 'articles': articles, 'alineas': alineas}
        return render(request, 'titrescpp.html', context)
    else:
        return render(request, 'error.html')

def code_procedure_penale(request):
    texteResponse = requests.get('http://127.0.0.1:8000/api/textes/?id=2')
    livreResponse = requests.get('http://127.0.0.1:8000/api/livres/?text=2&numero=')
    titreResponse = requests.get('http://127.0.0.1:8000/api/titres/?livre=1&numero=')
    chapResponse = requests.get('http://127.0.0.1:8000/api/chapitres/')
    secResponse = requests.get('http://127.0.0.1:8000/api/sections/')
    articleResponse = requests.get('http://127.0.0.1:8000/api/articles/')
    alineaResponse = requests.get('http://127.0.0.1:8000/api/alineas/')
    if texteResponse.status_code == 200 and livreResponse.status_code == 200 and titreResponse.status_code == 200 and chapResponse.status_code == 200 and secResponse.status_code == 200 and articleResponse.status_code == 200 and alineaResponse.status_code == 200:
        texte = texteResponse.json()
        livres = livreResponse.json()
        titres = titreResponse.json()
        chapters = chapResponse.json()
        sections = secResponse.json()
        articles = articleResponse.json()
        alineas = alineaResponse.json()
        context = {'texte': texte, 'livres': livres, 'titres': titres, 'chapters': chapters, 'sections': sections, 'articles': articles, 'alineas': alineas}
        return render(request, 'cpp.html', context)
    else:
        return render(request, 'error.html')


