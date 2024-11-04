lista = [8000, 7998, 7996, 7994, 7994]

numPares = list(filter(lambda x: x % 2 == 0, lista))
 
maioresPares = sorted(numPares, reverse = True)
 
soma = sum(maioresPares)
 
map(lambda i: i, lista)
 
print(str(maioresPares)+ str('\n')+ str(soma))