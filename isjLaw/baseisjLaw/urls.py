from django.urls import path
from . import views
from .views import Home, code_procedure_penale, code_penal, constitution, LoginPage, RegisterPage
from rest_framework import routers
from .views import TexteViewSet, LivreViewSet, TitreViewSet, ChapitreViewSet, SectionViewSet, ArticleViewSet, AlineaViewSet

from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from isjLaw import settings

router = routers.DefaultRouter()
router.register('textes', TexteViewSet)
router.register('livres', LivreViewSet)
router.register('titres', TitreViewSet)
router.register('chapitres', ChapitreViewSet)
router.register('sections', SectionViewSet)
router.register('articles', ArticleViewSet)
router.register('alineas', AlineaViewSet)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('code_penal/', code_penal, name='code_penal'),
    path('code_procedure_penale/', code_procedure_penale, name='code_procedure_penale'),
    path('constitution/', constitution, name='constitution'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
