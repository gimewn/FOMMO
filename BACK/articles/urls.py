from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_article), 
    path('<int:article_pk>/', views.get_detail), 
    path('create_article/', views.create_article), 
    path('<int:article_pk>/edit_article/', views.edit_article), 
    path('<int:article_pk>/delete_article/', views.delete_article), 
    path('<int:article_pk>/like_article/', views.like_article), 
    path('<int:article_pk>/create_comment/', views.create_comment), 
    path('<int:article_pk>/edit_comment/<int:comment_pk>/', views.edit_comment), 
    path('<int:article_pk>/delete_comment/<int:comment_pk>/', views.delete_comment), 

]
