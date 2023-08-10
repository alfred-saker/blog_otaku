from django import forms
import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):
  class Meta:
    model = Article
    fields = {
      'title': ['icontains'],
      'categorie': ['exact'],
      'genre': ['exact'],
    }

    labels = {
      'title': 'Titre de l\'article',
      'categorie': 'Categorie',
      'genre': 'Genre',
    }
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
      'categorie': forms.SelectMultiple(attrs={'class': 'form-control'}),
      'genre': forms.SelectMultiple(attrs={'class': 'form-control'}),
    }
