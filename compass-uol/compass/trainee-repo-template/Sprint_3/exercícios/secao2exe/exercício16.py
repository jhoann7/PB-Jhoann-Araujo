def soma_numeros_string(numeros_str):

  numeros_lista = numeros_str.split(',')

  soma = sum(int(numero) for numero in numeros_lista)

  return soma

numeros = "1,3,4,6,10,76"

resultado = soma_numeros_string(numeros)
print(resultado)