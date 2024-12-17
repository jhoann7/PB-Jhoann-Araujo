import requests as rq
import pandas as pd
from IPython.display import display

api_key = '91baff9936f6aec8786402b1e0734bd8'
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = rq.get(url)
data = response.json()

filmes = []

for movie in data['results']:
    df = {
        'Titulo' : movie['title'],
        'Data de lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos': movie['vote_average']
    }
    filmes.append(df)
    
    df = pd.DataFrame(filmes)
    display(df)