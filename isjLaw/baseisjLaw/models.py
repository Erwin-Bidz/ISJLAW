from django.db import models

# Create your models here.

class Texte(models.Model):
    nom = models.CharField(max_length=200)
    preambule = models.TextField(null=True, blank=True)
    numero_de_loi = models.CharField(max_length=50)
    adoption = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nom


class Livre(models.Model):
    text = models.ForeignKey(Texte, on_delete=models.CASCADE)
    numero = models.IntegerField(null=False)
    libelle = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.libelle

    class Meta:
        ordering = ['libelle']

class Titre(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, null=True)
    numero = models.IntegerField(null=False)
    libelle = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.libelle

class Chapitre(models.Model):
    titre = models.ForeignKey(Titre, on_delete=models.CASCADE)
    numero = models.IntegerField(null=False)
    libelle = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.libelle

class Section(models.Model):
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    numero = models.IntegerField(null=False)
    libelle = models.CharField(max_length=200)

    def __str__(self):
        return self.libelle

class Article(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    numero = models.IntegerField(null=False)
    libelle = models.CharField(max_length=200)

    def __str__(self):
        return self.libelle

class Alinea(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    #numero = models.CharField(max_length=200,null=False)
    numero = models.IntegerField(null=False)
    libelle = models.TextField()