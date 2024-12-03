# Etapa 1 - Arquivos csv.

![arquivoscsv](evidencias/arquivoscsv.png)

Eu comecei o desafio baixando os arquivos csv disponibilizado na plataforma da Udemy, depois os coloquei dentro da pasta "[arquivoscsv](desafio/arquivoscsv)"

# Etapa 2 - Enviando arquivos par o bucket.

![scriptPy](evidencias/scriptPy.png)

Na segunda etapa do desafio eu criei um script python para enviar os arquivos csv para o bucket da AWS, para fazer isso eu utilizei a biblioteca boto3, que é a biblioteca oficial para serviços da AWS. Eu começo o script informando a região "us-east-1" que é a região que o meu bucket está. Depois eu crio um cliente s3 com o "boto3.client" e coloco na variável s3_client. Depois eu dou um nome para o bucket, um nome para o arquivo e o caminho do objeto. Após isso, o script ira tentar criar um bucket na AWS caso não exista nenhum com o nome informado com o "head_bucket", como o bucket já existe, irá aparecer a mensagem da linha logo após no terminal "Bucket jhoannsprint6 já existe.". Depois de tudo isso, finalmente os arquivos são enviados para o bucket com o "upload_file" que caso envie corretamente irá aparecer uma menssagem de sucesso, caso contrário, uma menssagem de erro.

# Etapa 3 - Criando imagem e executando container.

## Dockerfile.

![dockerfile](evidencias/dockerfile.png)

No arquivo Dockerfile eu começo pelo "FROM" que define a imagem base a partir da qual eu irei construir a minha imagem, no meu caso, o python:3. No próximo passo eu usei o "WORKDIR", ele define o diretório de trabalho dentro da imagem, todos os comandos a seguir serão executados nesse diretório, no meu caso é a pasta "app", onde está o arquivo "carguru.py". Posteriormente vem o comando "COPY", ele tem a função de copiar arquivos do ambiente local para a imagem que está sendo construída, no meu caso eu estou copiando tudo e levando para a raiz do projeto. E por fim eu uso o "CMD" e dou o caminho para ele executar o meu script.

## Criando imagem.

![build](evidencias/build.png)

Para criar a imagem eu começo com o "docker build" que é o comando principal pra construir uma nova imagem a partir eu um Dockerfile, ele lê as instruções do Dockerfile linha por linha e executa cada uma delas para criar a imagem. O "-t" é uma flag que eu utilizei para por um nome na a imagem que eu irei criar. O "meubucket" é o nome que eu criei para a minha imagem. Por fim, este ponto não final não é pra dizer que acabou a "frase", ele está indicando que eu quero executar o build a partir do meu diretório atual.

![imagemCriada](evidencias/imagemCriada.png)

Acima, temos a imagem sendo criada sem nenhuma interrupção ou erro.

## Executando container.

![exeContainer](evidencias/exeContainer.png)

Para exercutar o container eu utilizo o comando docker run, como eu preciso das credenciais para acessar o bucket da AWS eu utilizo as minhas chaves de acesso, primeiro a pública, depois a privada e por fim o token de acesso, e no final tem o nome da imagem a partir da qual eu quero executar o meu container.

![containerExe](evidencias/containerExe.png)

Agora temos o container sendo executado com sucesso.

![dockerPs](evidencias/dockerPs.png)

Na imagem acima eu dei um "docker ps -a" para mostrar que o container foi criado.

# Etapa 3 - Mostrando o bucket da AWS.

![bucket](evidencias/bucketAWS.png)

Na primeira imagem temos o bucket que foi criado para a execução do desafio.

![movies](evidencias/movies.png)

Aqui eu tenho todo o caminho que foi pedido para chegar no arquivo "movies.csv"

![series](evidencias/series.png)

Por fim, temos todo o caminho para chegar no arquivo "series.csv"

# Essa foi a minha execução do desafio, tive bastante dificuldade na parte de credenciais, mas com ajuda do meu squad e do monitor da sprint eu consegui resolver os problemas. Espero ter executado o desafio da forma esperada.