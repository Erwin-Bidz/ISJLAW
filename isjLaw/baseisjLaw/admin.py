from django.contrib import admin
from .models import Texte, Livre, Titre, Chapitre, Section, Article, Alinea

# Register your models here.
#admin.site.register(Texte, Livre, Titre)
#admin.site.register(Chapitre, Section, Article)
#admin.site.register(Alinea)

@admin.register(Texte, Livre, Titre, Chapitre, Section, Article, Alinea)
class GenericAdmin(admin.ModelAdmin):
    pass
