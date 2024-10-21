numeros = []
for i in range(1, 4):
    numeros.append(i)
for num in numeros:
    par_impar = num % 2
    if par_impar == 0:
        print(f'Par: {num}')
    else:
        print(f'Ímpar: {num}')