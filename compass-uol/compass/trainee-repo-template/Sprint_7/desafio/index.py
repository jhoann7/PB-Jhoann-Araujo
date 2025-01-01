import requests
import json
import boto3
import os
import pandas as pd
from datetime import datetime

total_paginas = 10
todos_os_dados = []
filmes = []

for pagina in range(1, total_paginas + 1):
    api_key = os.environ.get('TMDB_API_KEY')
    id_genero = 14
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={id_genero}&page={pagina}"
    response = requests.get(url)
    dados = response.json()

    
    for filme in dados['results']:
        dados_filmes = {
            'id': filme['id'],
            'linguagemOriginal': filme['original_language'],
            'visaoGeral': filme['overview'],
            'tituloOriginal': filme['original_title'],
            'popularidade': filme['popularity'],
            'dataDeLancamento': filme['release_date'],
            'mediaDeVotos': filme['vote_average']
        }
        filmes.append(dados_filmes)

    todos_os_dados.extend(dados['results'])

meio =  len(filmes) // 2
filmes_parte1 = filmes[:meio]
filmes_parte2 = filmes[meio:]

file_name_part1 = 'filmes_parte1.json'
file_name_part2 = 'filmes_parte2.json'

date = datetime.now()
dia = date.day
mes = date.month
ano = date.year

region = 'us-east-1'
s3_client = boto3.client('s3', region_name=region)

file_name = 'filmes.json'
bucket_name = 'jhoannsprint6'
bucket_file_key = f'meubucket/Raw/TMDB/JSON/{ano}/{mes}/{dia}/{file_name}'
dados_json = json.dumps(filmes, indent=4)

for parte, filmes_parte in enumerate([filmes_parte1, filmes_parte2]):
    bucket_file_key = f'meubucket/Raw/TMDB/JSON/{ano}/{mes}/{dia}/{file_name_part1 if parte == 0 else file_name_part2}'
    dados_json = json.dumps(filmes_parte, indent=4)

    try:
        s3_client.put_object(Body=dados_json, Bucket=bucket_name, Key=bucket_file_key)
        print(f"Parte {parte+1} salva com sucesso em {bucket_name}/{bucket_file_key}")
    except Exception as e:
        print(f"Erro ao salvar a parte {parte+1} no S3: {e}")