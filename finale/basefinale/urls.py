from django.urls import path
from .views import FileList, FileDetail, FileAdd, PageLogin, EmployeAdd, CompanyAdd, FileDelete, FileUpdate, FileContent

from rest_framework import routers
from basefinale.views import EntrepriseViewSet, FichierViewSet, RegisterPage, EmployeViewSet
from django.contrib.auth.views import LogoutView

from django.urls import path, include
from django.conf.urls.static import static
#from django.conf import settings
from finale import settings

router = routers.DefaultRouter()
router.register('fichiers', FichierViewSet)
router.register('entreprise', EntrepriseViewSet)
router.register('employe', EmployeViewSet)

urlpatterns = [
    path('', PageLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('files/', FileList.as_view(), name='files'),
    path('fichier/<int:pk>', FileDetail.as_view(), name='fichier'),
    path('contenu/<int:pk>', FileContent.as_view(), name='contenu'),
    path('file_add/', FileAdd.as_view(), name='file_add'),
    path('file_update/<int:pk>/', FileUpdate.as_view(), name='file_update'),
    path('file_delete/<int:pk>/', FileDelete.as_view(), name='file_delete'),
    path('company_add/', CompanyAdd.as_view(), name='company_add'),
    path('new-employe/', EmployeAdd.as_view(), name='new-employe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
