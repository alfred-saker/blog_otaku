from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginForm, ChangeProfileImageForm, ChangeInfoUserForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

from django.core.paginator import Paginator
from articles.filters import ArticleFilter
from django.contrib import messages

from articles.models import Article, Categorie, Genre
from accounts_user.models import UserProfile


def home(request):
  articles = Article.objects.order_by('-created_at')
  filter = ArticleFilter(request.GET, queryset=articles)
  
  # Nombre d'articles à afficher par page
  items_per_page = 3
  # Créez un objet Paginator avec les articles et le nombre d'éléments par page
  paginator = Paginator(filter.qs, items_per_page)
  # Récupérez le numéro de page à partir des paramètres GET, par défaut à la première page (page 1)
  page_number = request.GET.get('page', 1)
  # Obtenez la page demandée à partir de l'objet Paginator
  page = paginator.get_page(page_number)
  
  context = {'page':page,'filter':filter}
  return render(request, 'accounts/home.html',context)

def register_view(request):
  forms = CreateUserForm()
  form = LoginForm(request.POST)
  if request.method == 'POST':
    forms = CreateUserForm(request.POST)
    if forms.is_valid():
      user = forms.save()
      username = forms.cleaned_data.get('username')
      messages.success(request, 'Votre compte à bien été crée'  + username)
      return redirect('login')
  context = {
    'forms':forms,
    'form':form,
    }
  return render(request, 'accounts/login.html',context)
  
def login_view(request):
  forms = CreateUserForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
      else:
        messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
  else:
    form = LoginForm()
  context = {
    'form':form,
    'forms':forms,
    }
  return render(request, 'accounts/login.html', context)

def logout_view(request):
  logout(request)
  return redirect('login')

@login_required(login_url='login')
def change_profile_image(request):
  user_profile = request.user.userprofile

  if request.method == 'POST':
    profil_image_form = ChangeProfileImageForm(request.POST, request.FILES, instance=user_profile)
    if profil_image_form.is_valid():
      profil_image_form.save()
      messages.success(request,"Avatar modifié avec success")
      return redirect('profile_user')
  else:
    image_form = ChangeProfileImageForm(instance=user_profile)
  context = {'image_form':image_form}
  return render(request, 'accounts/profil_user.html', context)

@login_required(login_url='login')
def change_info_user(request):
  user = request.user
  user_profile = request.user.userprofile

  image_form = ChangeProfileImageForm(instance=user_profile)

  if request.method == 'POST':
    user_form = ChangeInfoUserForm(request.POST, instance=user)
    if user_form.is_valid():
      user_form.save()
      messages.success(request,"Infos modifié avec success")
      return redirect('profile_user')
    else:
      print(user_form.errors)
  else:
    user_form = ChangeInfoUserForm(instance=user)

  context = {
    'user_form':user_form,
    'user_profile':user_profile
    }
  return render(request, 'accounts/profil_user.html', context)

@login_required(login_url='login')
def change_password(request):
  user = request.user
  user_form = ChangeInfoUserForm(instance=user)
  image_form = ChangeProfileImageForm()

  if request.method == 'POST':
    password_form = ChangePasswordForm(request.user,request.POST)
    if password_form.is_valid():
      password_form.save()
      update_session_auth_hash(request, user)
      messages.success(request,"Mot de passe  modifié avec success")
      return redirect('profile_user')
    else:
      print(password_form.errors)
  else:
    password_form = ChangePasswordForm(request.user)
  
  context = {
    'image_form':image_form,
    'user_form':user_form,
    'password_form':password_form
  }
  return render(request, 'accounts/profil_user.html', context)

@login_required(login_url='login')
def profil_user(request):

  user = request.user
  user_profile = request.user.userprofile
  image_form = ChangeProfileImageForm()
  password_form = ChangePasswordForm(request.user)
  user_form = CreateUserForm(instance=user)
  nbre_article = Article.objects.filter(author=user).count()

  nbre_categorie = Categorie.objects.filter(article__author=user).distinct().count()

  nbre_genre = Genre.objects.filter(article__author=user).distinct().count()

  context = {
    'user_form':user_form,
    'image_form':image_form,
    'password_form':password_form,
    'user_profile':user_profile,
    'nbre_article':nbre_article,
    'nbre_categorie':nbre_categorie,
    'nbre_genre':nbre_genre
  }
  return render(request, 'accounts/profil_user.html', context)