primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, (nome, sobrenome, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f'{i} - {nome} {sobrenome} está com {idade} anos')