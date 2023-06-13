from django.urls import path
from . import views
from .views import livres_cpp_view, titres_cpp_view, Home, code_procedure_penale
from rest_framework import routers
from .views import TexteViewSet, LivreViewSet, TitreViewSet, ChapitreViewSet, SectionViewSet, ArticleViewSet, AlineaViewSet

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
    path('code_procedure_penale/', code_procedure_penale, name='code_procedure_penale'),
    path('livrescpp/', livres_cpp_view, name='livrescpp'),
    path('titrescpp/', titres_cpp_view, name='titrescpp')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
