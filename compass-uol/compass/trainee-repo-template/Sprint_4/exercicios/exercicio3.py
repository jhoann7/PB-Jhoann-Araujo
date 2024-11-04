from functools import reduce
def calcula_saldo(lancamentos) -> float:

    valores = list(map(lambda i: i[0] if i[1] == 'C' else -i[0], lancamentos))
    saldo = reduce(lambda i, c: i + c, valores)

    return saldo
 