import json
 
def lambda_handler(event, context):

    import requests
    import boto3

    api_key = "91baff9936f6aec8786402b1e0734bd8"
    genero_id = 14
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genero_id}"

    def obter_filmes(genero_id):
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
                'lingua_original': filme['original_language'],
            }
            filmes.append(dados_filmes)
        dados_json = json.dumps(filmes, indent=4)
        
        region = 'us-east-1'
        s3_client = boto3.client('s3', region_name=region)

        file_name = 'filmes.json'
        bucket_name = 'jhoannsprint6'
        bucket_file_key = 'meubucket/Raw/TMDB/JSON/2024/12/11/filmes.json'

        try:
            s3_client.put_object(Body=dados_json, Bucket=bucket_name, Key=bucket_file_key)
            print(f"Dados salvos com sucesso em {bucket_name}/{bucket_file_key}")
        except Exception as e:
            print(f"Erro ao salvar os dados no S3: {e}")

        return filmes
    obter_filmes(genero_id)
    return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }