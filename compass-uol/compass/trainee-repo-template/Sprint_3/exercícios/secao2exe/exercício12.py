def my_map(lista, funcao):

    nova_lista = []
    for elemento in lista:
        resultado = funcao(elemento)
        nova_lista.append(resultado)
    return nova_lista

def elevar_ao_quadrado(x):
    return x**2


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


resultados = my_map(numeros, elevar_ao_quadrado)

print(resultados)