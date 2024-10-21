with open('actors.csv', 'r') as arquivocsv, open('etapa-1.txt', 'w') as arquivotxt, open('etapa-2.txt', 'w') as arquivo2, open('etapa-3.txt', 'w') as arquivo3, open('etapa-4.txt', 'w') as arquivo4, open('etapa-5.txt', 'w') as arquivo5:
    linhas = arquivocsv.readlines()
    linhas = linhas[1:]

    mais_filmes = ''
    ator_mais_filmes = ''

    soma_bilheteria = 0
    num_filmes = 0

    maior_media = 0
    ator_maior_media = 0

    contagem_filmes = {}
    
    atores_receitas = []

    for linha in linhas:
        dados = linha.strip().split(',')
        nome = dados[0]
        num_filmes_ator = dados[2]
        bilheteria_filme_principal = dados[-1]

        bilheteria_filme_principal = float(bilheteria_filme_principal)

        total_gross = float(dados[-5])
        atores_receitas.append((nome, total_gross))

        if num_filmes_ator > mais_filmes:
            mais_filmes = num_filmes_ator
            ator_mais_filmes = nome
    
        soma_bilheteria += bilheteria_filme_principal
        num_filmes += 1
        media_bilheteria = soma_bilheteria / num_filmes

    for linha in linhas:
        dados = linha.strip().split(',')
        nome = dados[0]
        media_por_filme = float(dados[3])

        if media_por_filme > maior_media:
            maior_media = media_por_filme
            ator_maior_media = nome

    for linha in linhas:
        dados = linha.strip().split(',')
        filme = dados[4]

        if filme in contagem_filmes:
            contagem_filmes[filme] += 1
        else:
            contagem_filmes[filme] = 1
    
    
    filmes = []
    quantidades = []
    for filme, quantidade in contagem_filmes.items():
        filmes.append(filme)
        quantidades.append(quantidade)
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda item: item[1], reverse=True)
    
    for filme, quantidade in filmes_ordenados:
        arquivo4.write(f'O filme {filme} aparece {quantidade} vez(es) no dataseat. \n')
  
    
    atores_ordenados = sorted(atores_receitas, key=lambda x: x[1], reverse=True)
    for ator, receita in atores_ordenados:
        arquivo5.write(f'{ator} - {receita}\n')

    print(f'O ator com mais filmes é: {ator_mais_filmes} com {mais_filmes} filmes.', file=arquivotxt)
    print(f'A média da bilheteria bruta dos filmes principais é: {media_bilheteria:.2f}', file=arquivo2)
    print(f'O ator com maior média de receita bruta de bilheteria é {ator_maior_media}', file=arquivo3)