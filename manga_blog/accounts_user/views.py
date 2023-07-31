from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

from django.core.paginator import Paginator
from articles.filters import ArticleFilter
from django.contrib import messages

from articles.models import Article, Categorie, Genre

# Create your views here.
# @login_required(login_url='login')
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
  form = CreateUserForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, 'Votre compte à bien été crée'  + username)
      return redirect('login')
  context = {'form':form}
  return render(request, 'accounts/register.html',context)
  
def login_view(request):
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
  context = {'form':form}
  return render(request, 'accounts/login.html', context)

def logout_view(request):
  logout(request)
  return redirect('login')

def profil_user(request):
  user = request.user

  nbre_article = Article.objects.count()

  nbre_categorie = Categorie.objects.count()

  nbre_genre = Genre.objects.count()

  context = {
    'user':user,
    'nbre_article':nbre_article,
    'nbre_categorie':nbre_categorie,
    'nbre_genre':nbre_genre
  }
  return render(request, 'accounts/profil_user.html', context)
