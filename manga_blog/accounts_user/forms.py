from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms

class CreateUserForm(UserCreationForm):

  class Meta:
    model = User
    fields = ['username','email','password1','password2']

    labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse e-mail',
            'password1': 'Mot de passe',
            'password2': 'Confirmer le mot de passe',
    }
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
      'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Votre adresse mail'}),
      'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
      'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'}),
    }

class ChangePasswordForm(PasswordChangeForm):

  class Meta:
    model = User
    fields = '__all__'
    labels = {
            'old_password': 'Ancien Mot de passe',
            'new_password1': 'Nouveau mot de passe',
            'new_password2': 'Confirmer le mot de passe',
    }
    widgets = {
      'old_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ancien Mot de passe'}),
      'new_password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nouveau mot de passe'}),
      'new_password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'}),
    }

class ChangeInfoUserForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ['username','email']
    exclude = ['password1','password2']

    labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse e-mail',
    }
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer votre Username'}),
      'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Votre adresse mail'})
    }

class ChangeProfileImageForm(forms.ModelForm):
    class Meta:
      model = UserProfile
      fields = ['avatar']
      widgets = {
        'avatar': forms.FileInput(attrs={'class': 'form-control'}),
      }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse e-mail',
    }
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
      'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Votre adresse mail'}),
    }


    