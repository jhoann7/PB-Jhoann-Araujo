import json

with open('person.json', 'r') as arquivo:
    dados = json.load(arquivo)

json_string = json.dumps(dados)
com_asp_simples = json_string.replace('"', "'")

print(com_asp_simples)