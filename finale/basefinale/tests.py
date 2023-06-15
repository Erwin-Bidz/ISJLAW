from django.test import TestCase
from basefinale.models import Entreprise, Fichier

# Create your tests here.
class EntrepriseTestCase(TestCase):

    def test_create_company(self):
        nbr_entreprises_avt_ajout = Entreprise.objects.count()

        new_Entreprise = Entreprise()
        new_Entreprise.name = 'my_first_company'
        new_Entreprise.save()

        nbr_entreprises_apr_ajout = Entreprise.objects.count()

        self.assertTrue(nbr_entreprises_apr_ajout == nbr_entreprises_avt_ajout + 1)