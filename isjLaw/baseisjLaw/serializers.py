from rest_framework import serializers
from .models import Texte, Livre, Titre, Chapitre, Section, Article, Alinea

class TexteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Texte
        fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Livre
        fields = '__all__'

class TitreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Titre
        fields = '__all__'

class ChapitreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Chapitre
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Section
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'

class AlineaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Alinea
        fields = '__all__'