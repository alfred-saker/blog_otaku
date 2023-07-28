from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categorie(models.Model):
  categorie = models.CharField(max_length=200)
  description = models.CharField(max_length=1000, null=True)
  image_categorie = models.ImageField(upload_to='categorie_images/', blank=True, null=True)

  def __str__(self):
    return self.categorie

class Tag(models.Model):
  tag = models.CharField(max_length=200)

  def __str__(self):
    return self.tag

class Genre(models.Model):
  genre = models.CharField(max_length=200)

  def __str__(self):
    return self.genre

class Article(models.Model):

  title = models.CharField(max_length=200)
  sous_content = models.CharField(max_length=1000, blank=True)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  publication_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image_article = models.ImageField(upload_to='article_images/', blank=True, null=True)
  categorie = models.ManyToManyField(Categorie)
  tag = models.ManyToManyField(Tag)
  genre = models.ManyToManyField(Genre)

  def __str__(self):
    return self.title
