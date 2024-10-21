def dividir_lista(lista):

  tamanho = len(lista)
  terco = tamanho // 3

  parte1 = lista[:terco]
  parte2 = lista[terco:terco*2]
  parte3 = lista[terco*2:]

  resultado_formatado = f"[{', '.join(map(str, parte1))}] [{', '.join(map(str, parte2))}] [{', '.join(map(str, parte3))}]"
  return resultado_formatado

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

resultado = dividir_lista(lista)
print(resultado)
