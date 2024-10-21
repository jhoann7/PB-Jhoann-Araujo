for num in range(2, 101):
  número_primo = True
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      número_primo = False
      break
  if número_primo:
    print(num)