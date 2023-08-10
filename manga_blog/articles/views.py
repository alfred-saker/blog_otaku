from django.shortcuts import render,redirect,get_object_or_404

from django.core.paginator import Paginator
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .form import ArticleForm,CategorieForm,CommentForm

from .models import *

# Create your views here.

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login') 
def add_categorie(request):
  if request.method == 'POST':
    form = CategorieForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.info(request, 'Categorie créee avec success')
      return redirect('all_categorie')
  else:
    form = CategorieForm()
  context = {'form':form}
  return render(request, 'articles/categorie_form.html', context)

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
  articles_limit = Article.objects.all().order_by('-created_at')[:3]

  get_articles = get_object_or_404(Article, id=id)
  categories = get_articles.categorie.all()
  # categories = Categorie.objects.all()
  get_comment = Comment.objects.filter(article=get_articles)
  # print(get_comment.user)
  form_comment = CommentForm()

  context = {
    'get_comment':get_comment,
    'get_articles':get_articles,
    'categories':categories,
    'articles_limit':articles_limit,
    'form_comment':form_comment,
    }
  return render(request, 'articles/details_articles.html', context)


def article_by_categorie(request,id):

  category = get_object_or_404(Categorie, id=id)
  articles = category.article_set.all()
  # category = Categorie.objects.get(id=id)
  print(category)
  # articles = Article.objects.filter(categorie=category)

  # Nombre d'articles à afficher par page
  items_per_page = 3
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

# @login_required(login_url='login')
def create_comment(request,id):
  get_articles = get_object_or_404(Article, id=id)
  articles_limit = Article.objects.all().order_by('-created_at')[:3]

  categories = Categorie.objects.all()

  article_id = request.POST['article_id']
  print(article_id)
  if request.user.is_authenticated:
    if request.method == 'POST':
      form_comment = CommentForm(request.POST)
      if form_comment.is_valid():
        comment = form_comment.save(commit=False)
        comment.user = request.user
        comment.article = Article.objects.get(id=article_id)
        comment.save()
        return redirect('details_articles', id=article_id)
    else:
      form_comment = CommentForm()
  else:
    messages.info(request, "Veuillez vous connectez pour commenter cet article")
    return redirect('details_articles',id=article_id)
  
  context = {
    'form_comment':form_comment,
    'get_articles':get_articles,
    'categories':categories,
    'articles_limit':articles_limit,
    }
  return render(request, 'articles/details_articles.html',context)


