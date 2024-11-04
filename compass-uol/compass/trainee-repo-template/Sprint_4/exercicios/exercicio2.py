def conta_vogais(texto:str)-> int:
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return len(list(filter(lambda letra: letra in vogais, texto)))
    numVogais = conta_vogais(vogais)
    