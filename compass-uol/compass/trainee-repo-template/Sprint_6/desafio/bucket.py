import boto3

region = 'us-east-1'
s3_client = boto3.client('s3', region_name=region)
 
file_name = 'arquivoscsv/movies.csv'
file2_name = 'arquivoscsv/series.csv'
bucket_name = 'jhoannsprint6'
bucket_file_key = 'meubucket/Raw/Local/CSV/Movies/2024/11/27/movies.csv'
bucket2_file_key = 'meubucket/Raw/Local/CSV/Series/2024/11/27/series.csv'

try:
    s3_client.head_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' já existe.")
except s3_client.exceptions.ClientError:
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar o bucket: {e}")
        exit(1)  

try:
    s3_client.upload_file(file_name, bucket_name, bucket_file_key)

    print(f"Arquivo '{file_name}' carregado no bucket '{bucket_name}' com sucesso.")

    s3_client.upload_file(file2_name, bucket_name, bucket2_file_key)

    print(f"Arquivo '{file2_name}' carregado no bucket '{bucket_name}' com sucesso.")

except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")