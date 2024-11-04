import csv
 
with open('estudantes.csv', 'r') as arquivoCsv:
    readerCsv = csv.reader(arquivoCsv)
    data = list(readerCsv)
 
relatorio = []

for linha in data:
    nome = linha[0]
    notas = list(map(int, linha[1:]))
    tres_maiores = sorted(notas, reverse=True)[:3]
    media = round(sum(tres_maiores) / 3, 2)

    relatorio.append((nome, tres_maiores, media))
 
relatorio.sort(key=lambda x: x[0])
 
for nome, tres_maiores, media in relatorio:

    print(f"Nome: {nome} Notas: {tres_maiores} Média: {media}")

 