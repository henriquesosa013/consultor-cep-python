import requests
from os import system
from time import sleep
from datetime import datetime

hora = datetime.now().strftime("%H:%M:%S")
while True:
    print("\n1 - Consultar CEP")
    print("2 - Ver histórico")
    print("3 - Sair")
    try:
        opcao = int(input("\nEscolha uma opção:"))
    except:
        print("apenas numeros!")
        sleep(4)
        system("cls")
        continue
        

    if opcao == 1:
        cep = str(input("Qual cep deseja consultar:").replace("-", ""))
        url = (f"https://viacep.com.br/ws/{cep}/json/")
        resposta = requests.get(url)
        dados = resposta.json()

        print(f"Rua:{dados["logradouro"]}")
        print(f"Bairro:{dados["bairro"]}")
        print(f"Cidade:{dados["localidade"]}")
        print(f"Estado:{dados["uf"]}")

        print()

        with open("historico.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{hora} {cep} - {dados['logradouro']} - {dados['bairro']} - {dados['localidade']} - {dados['uf']}\n")
        sleep(5)

    elif opcao == 2:
        with open ("historico.txt", "r", encoding="utf-8") as hist:
            for linha in hist:
                print(linha.strip())
        sleep(5)
    
    elif opcao == 3:
        system("cls")
        break
