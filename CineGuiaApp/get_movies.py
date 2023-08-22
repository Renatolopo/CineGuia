# documentação
# https://github.com/AnthonyBloomer/tmdbv3api


from tmdbv3api import TMDb
from tmdbv3api import Movie 
tmdb=TMDb()
from CineGuiaApp.models import Filme



def fetch_data_from_api():
    api_key = '902e49cad52ce6693e739d4996a2e8a0'
    TMDb.api_key = api_key
    tmdb.language = 'pt-br'
    tmdb.debug = True
    movie=Movie()
    
    return movie
    
def populate_items_from_api():

    movie = fetch_data_from_api()
    api_data = movie.popular(page=50)
    

    for filme_data in api_data:
        try:
            item = Filme(id_filme = filme_data.id, 
                        title = filme_data.title,
                        descricao = filme_data.overview,
                        img = filme_data.poster_path,
                        avaliacao = filme_data.vote_average)
            
            item.save()
        except:
            continue

def search_movie(name):
    api_data = fetch_data_from_api()
    api_data = api_data.search(name)
    for filme_data in api_data:
        try:
            item = Filme(id_filme = filme_data.id, 
                        title = filme_data.title,
                        descricao = filme_data.overview,
                        img = filme_data.poster_path,
                        avaliacao = filme_data.vote_average)
            
            item.save()
        except:
            continue


def search_genero(name):
    api_data = fetch_data_from_api()
    api_data = api_data.search(name)
    for filme_data in api_data:
        try:
            item = Filme(id_filme = filme_data.id, 
                        title = filme_data.title,
                        descricao = filme_data.overview,
                        img = filme_data.poster_path,
                        avaliacao = filme_data.vote_average)
            
            item.save()
        except:
            continue

def search_similar(id_movie):
    api_data = fetch_data_from_api()
    api_data = api_data.similar(int(id_movie))
    for filme_data in api_data:
        try:
            item = Filme(id_filme = filme_data.id, 
                        title = filme_data.title,
                        descricao = filme_data.overview,
                        img = filme_data.poster_path,
                        avaliacao = filme_data.vote_average,
                        similar_id = id_movie)
            
            item.save()
        except:
            continue
           
