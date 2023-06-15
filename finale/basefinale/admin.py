from django.contrib import admin
from basefinale.models import Entreprise, Fichier, Employe

# Register your models here.
@admin.register(Entreprise, Fichier)
class GenericAdmin(admin.ModelAdmin):
    pass

@admin.register(Employe)
class GenericAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'user', 'company', 'identifier')