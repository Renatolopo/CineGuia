from django.urls import path
from .views import index, atualizar_filmes_em_destaque, search_results, filmes

urlpatterns = [

    path('', index, name='index'),
    path('atualizar-filmes-em-destaque/', atualizar_filmes_em_destaque, name='atualizar_filmes_em_destaque'),
    path('search/', search_results, name='search_results'),
    path('filmes/', filmes, name='filmes'),
]