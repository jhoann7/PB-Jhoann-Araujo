def calcular_valor_maximo(operadores, operandos) -> float:

    # Mapeamento de operações como funções lambda

    operacoes = {

        '+': lambda x, y: x + y,

        '-': lambda x, y: x - y,

        '*': lambda x, y: x * y,

        '/': lambda x, y: x / y if y != 0 else float('-inf'),  # Evita divisão por zero

        '%': lambda x, y: x % y if y != 0 else float('-inf')   # Evita módulo por zero

    }
 
    # Aplicação das operações usando map

    resultados = list(map(lambda op_par: operacoes[op_par[0]](*op_par[1]), zip(operadores, operandos)))
 
    # Retorna o maior valor obtido

    return max(resultados)

 