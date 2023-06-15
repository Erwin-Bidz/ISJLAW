from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entreprise(models.Model):

    name = models.CharField(max_length=200, unique=True)


    def __str__(self):
        return self.name



class Fichier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(unique=True,max_length=200)
    favourite = models.BooleanField()
    upload_date = models.DateField(auto_now_add=True)
    content = models.FileField(upload_to='public', null=True)
    company = models.ForeignKey("Entreprise", on_delete=models.CASCADE)

    def __str__(self):
            return self.title

    class Meta:
        ordering = ['-id']


class Employe(models.Model):
    matricule = models.BigAutoField(auto_created=True, primary_key=True, editable=True, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=200, unique=True, null=False)

    #def __str__(self):
            #return self.matricule
