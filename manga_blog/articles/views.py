from django.shortcuts import render,redirect,get_object_or_404

from django.core.paginator import Paginator
from django.contrib import messages

from .form import ArticleForm

from .models import *

# Create your views here.

def add_articles(request):
  print(request.user)
  if request.method == 'POST':
    form = ArticleForm(request.POST,request.FILES)
    if form.is_valid():
      form.instance.author_id = request.user.id
      form.save()
      messages.info(request, 'Votre article a été créee avec success')
      return redirect('home')
  else:
    form = ArticleForm()
    print(form)

  context = {'form':form}
  return render(request, 'articles/article_form.html',context)

def edit_articles(request,id):
  article = Article.objects.get(id=id)
  form = ArticleForm(instance=article)

  if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      messages.success(request, 'Votre article a été modifiée avec success')
      return redirect('home')
  context = {'form':form}
  return render(request, 'articles/article_form.html',context)

def delete_articles(request, id):
  article = get_object_or_404(Article, id=id)
  article.delete()
  messages.info(request, 'Article supprimé')

    # Rediriger vers la page de confirmation ou autre vue après la suppression
  return redirect('home')
def categorie(request):
  categories = Categorie.objects.all().order_by('categorie')
  # Nombre d'articles à afficher par page
  items_per_page = 6
  # Créez un objet Paginator avec les articles et le nombre d'éléments par page
  paginator = Paginator(categories, items_per_page)
  # Récupérez le numéro de page à partir des paramètres GET, par défaut à la première page (page 1)
  page_number = request.GET.get('page', 1)
  # Obtenez la page demandée à partir de l'objet Paginator
  page = paginator.get_page(page_number)
  print(categories)

  context = {'page':page}
  return render(request, 'articles/categories.html', context)

def details_articles(request,id):
  articles_limit = Article.objects.order_by('-created_at')[:3]

  get_articles = get_object_or_404(Article, id=id)

  categories = Categorie.objects.all()

  categorie_article = Categorie.objects.get(id=id)

  context = {
    'get_articles':get_articles,
    'categories':categories,
    'categorie_article':categorie_article,
    'articles_limit':articles_limit
    }
  return render(request, 'articles/details_articles.html', context)

def article_by_categorie(request,id):
  category = Categorie.objects.get(id=id)
  articles = Article.objects.filter(categorie=category)

  # Nombre d'articles à afficher par page
  items_per_page = 2
  # Créez un objet Paginator avec les articles et le nombre d'éléments par page
  paginator = Paginator(articles, items_per_page)
  # Récupérez le numéro de page à partir des paramètres GET, par défaut à la première page (page 1)
  page_number = request.GET.get('page', 1)
  # Obtenez la page demandée à partir de l'objet Paginator
  page = paginator.get_page(page_number)

  context = {
    'category':category,
    'page':page,
  }

  return render(request, 'articles/articles_by_categorie.html',context)
