from django.forms import ModelForm
from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = '__all__'
    exclude = ['create_at','update_at','author']

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'article'}),
      'sous_content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sous-contenu de l\'article'}),
      'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Contenu de l\'article'}),
      # 'author': forms.HiddenInput(),
      'publication_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date de publication','type': 'datetime-local'}),
      'image_article': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Image de l\'article'}),
      'categorie': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Catégories'}),
      'tag': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Tags'}),
      'genre': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Genres'}),
        }