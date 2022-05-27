from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_movies),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/get_comment/', views.get_comment),
    path('<int:movie_pk>/create_comment/', views.create_comment),
    path('<int:movie_pk>/edit_comment/<int:comment_pk>/', views.edit_comment),
    path('<int:movie_pk>/delete_comment/<int:comment_pk>/', views.delete_comment),
    path('<int:movie_pk>/like_movie/', views.like_movie),
    path('<int:movie_pk>/check_like/', views.check_like),
    path('reco_movie/', views.reco_movie)
    
]
