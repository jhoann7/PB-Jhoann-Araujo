import csv

animais = ["cachorro", "gato", "periquito", "papagaio", "zebra", "tigre", "macaco", "camelo", "peixe", "cobra",
           "rato", "cavalo", "vaca", "ovelha", "porco", "galinha", "pato", "coelho", "anta", "tartaruga"]

animais_ordenados = sorted(animais)
[print(animal) for animal in animais_ordenados]

with open('animais.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for animal in animais_ordenados:
        writer.writerow([animal])