import random

random_list = random.sample(range(500), 50)
random_list.sort()

valor_minimo = min(random_list)
valor_maximo = max(random_list)
soma = sum(random_list)

media = soma / len(random_list)

if len(random_list) % 2 == 0:
    
  meio = len(random_list) // 2
  mediana = (random_list[meio - 1] + random_list[meio]) / 2
  
else:
    
  meio = len(random_list) // 2
  mediana = random_list[meio]

print(f"Media: {media:.2f}, Mediana: {mediana:.1f}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")