from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import Texte, Livre, Titre, Chapitre, Section, Article, Alinea
from .serializers import TexteSerializer, LivreSerializer, TitreSerializer, ChapitreSerializer, SectionSerializer, ArticleSerializer, AlineaSerializer

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
import requests
from django.urls import reverse_lazy

# Create your views here.

class Home(ListView):

    model = Texte
    template_name = 'home.html'
    context_object_name = 'textes'

class LoginPage(LoginView):
    template_name = 'baseisjLaw/login.html'
    fiels = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView):
    template_name = 'baseisjLaw/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('constitution')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
        ##S'assurer ici que l'utilisateur est authentifié

    #def get(self, *args, **kwargs):
    #    if self.request.user.is_authenticated:
    #        return redirect('home')
    #    return super(RegisterPage, self).get(*args, **kwargs)

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
    filterset_fields = ['article', 'numero', 'libelle']



# def code_penal(request):
#     texteResponse = requests.get('http://127.0.0.1:8000/api/textes/?id=1')
#     livreResponse = requests.get('http://127.0.0.1:8000/api/livres/?text=1&numero=')
#     titreResponse = requests.get('http://127.0.0.1:8000/api/titres/')
#     chapResponse = requests.get('http://127.0.0.1:8000/api/chapitres/')
#     secResponse = requests.get('http://127.0.0.1:8000/api/sections/')
#     articleResponse = requests.get('http://127.0.0.1:8000/api/articles/')
#     alineaResponse = requests.get('http://127.0.0.1:8000/api/alineas/')
#     if texteResponse.status_code == 200 and livreResponse.status_code == 200 and titreResponse.status_code == 200 and chapResponse.status_code == 200 and secResponse.status_code == 200 and articleResponse.status_code == 200 and alineaResponse.status_code == 200:
#         texte = texteResponse.json()
#         livres = livreResponse.json()
#         titres = titreResponse.json()
#         chapters = chapResponse.json()
#         sections = secResponse.json()
#         articles = articleResponse.json()
#         alineas = alineaResponse.json()
#         context = {'texte': texte, 'livres': livres, 'titres': titres, 'chapters': chapters, 'sections': sections, 'articles': articles, 'alineas': alineas}
#         return render(request, 'cp.html', context)
#     else:
#         return render(request, 'error.html')

def code_penal(request):
    search_term = request.POST.get('search_term')
    texteResponse = requests.get('http://127.0.0.1:8000/api/textes/?id=1')
    livreResponse = requests.get('http://127.0.0.1:8000/api/livres/?text=1&numero=')
    titreResponse = requests.get('http://127.0.0.1:8000/api/titres/')
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
        context = {'texte': texte, 'livres': livres, 'titres': titres, 'chapters': chapters, 'sections': sections, 'articles': articles, 'alineas': alineas, 'search_term': search_term}
        return render(request, 'cp.html', context)
    else:
        return render(request, 'error.html')

def code_procedure_penale(request):
    search_term = request.POST.get('search_term')
    if search_term is None:
        search_term = ' '

    texteResponse = requests.get('http://127.0.0.1:8000/api/textes/?id=2')
    livreResponse = requests.get('http://127.0.0.1:8000/api/livres/?text=2&numero=')
    titreResponse = requests.get('http://127.0.0.1:8000/api/titres/')
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
        context = {'texte': texte, 'livres': livres, 'titres': titres, 'chapters': chapters, 'sections': sections, 'articles': articles, 'alineas': alineas, 'search_term': search_term}
        return render(request, 'cpp.html', context)
    else:
        return render(request, 'error.html')

def constitution(request):
    search_term = request.POST.get('search_term')
    texteResponse = requests.get('http://127.0.0.1:8000/api/textes/?id=3')
    livreResponse = requests.get('http://127.0.0.1:8000/api/livres/?text=3&numero=')
    titreResponse = requests.get('http://127.0.0.1:8000/api/titres/')
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
        context = {'texte': texte, 'livres': livres, 'titres': titres, 'chapters': chapters, 'sections': sections, 'articles': articles, 'alineas': alineas, 'search_term': search_term}
        return render(request, 'constitution.html', context)
    else:
        return render(request, 'error.html')
