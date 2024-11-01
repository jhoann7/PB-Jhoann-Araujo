import hashlib 

opcao = 'S'

while opcao == 'S':
    string = str(input("Insira uma string: "))
    hashString = hashlib.sha1()
    hashString.update(string.encode('utf-8'))
    stringFinal = hashString.hexdigest()
    print(stringFinal)
    opcao = input("Quer inserir outra string? [S] ou [N] ").strip().upper()

    if opcao == 'N':
        print("Volte sempre :) ")
        break
    elif opcao != 'S' and opcao != 'N':
        print("Opção inválida!")