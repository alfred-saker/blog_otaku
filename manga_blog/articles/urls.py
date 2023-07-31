from django.urls import path

from .import views

urlpatterns = [
  path('add_articles/',views.add_articles,name="add_article"),

  path('edit_articles/<int:id>',views.edit_articles,name="edit_article"),

  path('delete_articles/<int:id>',views.delete_articles,name="delete_article"),

  path('add_categorie', views.add_categorie, name="add_categorie"),
  
  path('all_categorie/', views.categorie,name="all_categorie"),

  path('category_by_article/<int:id>/',views.article_by_categorie,name="categorie_by_article"),
  
  path('details/<int:id>/',views.details_articles, name="details_articles"),
]