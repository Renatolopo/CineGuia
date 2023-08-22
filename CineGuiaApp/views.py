from django.shortcuts import render
from .models import Filme
from .get_movies import populate_items_from_api, search_movie, search_similar
from django.http import JsonResponse

# Create your views here.
def index(request):
    context = {

    'filmes': Filme.objects.all()

    }
    return render(request,'index.html',context)


def atualizar_filmes_em_destaque(request):
    populate_items_from_api()
    response_data = {"message": "Filmes em destaque atualizados com sucesso!"}
    return JsonResponse(response_data)

def search_results(request):
    
    query = request.GET.get('q')  # Obtém o termo de pesquisa da query string
    search_movie(query)
    resultados = Filme.objects.filter(title__icontains=query)  # Filtra os filmes pelo título que contém o termo de pesquisa
    context = {'resultados': resultados}
    return render(request, 'search_results.html', context)

# def filme_categoria(request):
#     search_genero()
#     resultados = Filme.objects.filter(title__icontains=query)  # Filtra os filmes pelo título que contém o termo de pesquisa
#     context = {'resultados': resultados}
#     return render(request, 'search_results.html', context)

def filmes(request):
    filmes = Filme.objects.all()
    filme_id = request.GET.get('filme_id')  # Acessando o parâmetro filme_id da URL
    search_similar(filme_id)
    resultados = Filme.objects.filter(similar_id=filme_id) 
    context = {'resultados': resultados, 'filmes': filmes, 'filme_id': filme_id}
    return render(request, 'filmes.html', context)