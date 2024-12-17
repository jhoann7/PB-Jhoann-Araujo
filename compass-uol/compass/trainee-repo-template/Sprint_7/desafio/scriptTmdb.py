import requests
import boto3
import json

api_key = "91baff9936f6aec8786402b1e0734bd8"
genero_id = 14
url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genero_id}"

def obter_filmes(genero_id, paina=1, total_paginas=3):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genero_id}"
    resposta = requests.get(url)
    dados = resposta.json()

    filmes = []
    for filme in dados['results']:
        dados_filmes = {
            'titulo': filme['title'],
            'data_de_lancamento': filme['release_date'],
            'sinopse': filme['overview'],
            'caminho_do_poster': filme['poster_path'],
            'popularidade': filme['popularity'],
            'lingua_original': filme['original_language']
        }
        filmes.append(dados_filmes)
    dados_json = json.dumps(filmes, indent=4)
    return filmes

def salvar_no_s3(filmes, bucket_name, prefixo):
    region = 'us-east-1'
    s3_client = boto3.client('s3', region_name=region)

    for i in range(0, len(filmes), 100):
        grupo_filmes = filmes[i:i+100]
        dados_json = json.dumps(filmes, indent=4)
        file_name = f"{prefixo}_{i}.json"
        bucket_file_key = f'meubucket/Raw/TMDB/JSON/2024/12/11/{file_name}'

        try:
            s3_client.put_object(Body=dados_json, Bucket=bucket_name, Key=bucket_file_key)
            print(f"Dados salvos com sucesso em {bucket_name}/{bucket_file_key}")
        except Exception as e:
            print(f"Erro ao salvar os dados no S3: {e}")
genero_id = 14
total_paginas = 3
bucket_name = 'jhoannsprint100'
prefixo = 'filmes'

todos_filmes = []
for pagina in range(1, total_paginas + 1):
    filmes_pagina = obter_filmes(genero_id, pagina)
    todos_filmes.extend(filmes_pagina)

salvar_no_s3(todos_filmes, bucket_name, prefixo)