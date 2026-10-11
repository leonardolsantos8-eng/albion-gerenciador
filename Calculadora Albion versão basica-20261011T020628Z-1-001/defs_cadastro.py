import json



def iniciar_cadastro_itens():
    teste = json_stuff()
    print(teste)


def cadastro_itens(cadastro_dicionario):
    nome = input("Informe nome do iten: ")
    nutricao = float(input("Informe Nutriçao por porçao: "))
    rendimento = int(input("Informe rendimento final: "))
    #artefatos = input("Craft com artefatos? s|n: ")
    cadastro_dicionario = componetes_itens(nome,nutricao,rendimento,cadastro_dicionario)
    return cadastro_dicionario


def componetes_itens(nome,nutricao,rendimento,cadastro_dicionario):
    dic = cadastro_dicionario
    if not dic:
        cadastro_dicionario = {}
    cadastro_dicionario[nome] = {}
    while True:
        material = input("Informe nome do material: 'sair' para sair: ")
        if material == "sair":
            break
        quantidade = float(input("Informe quantidade do mateiral: "))
        cadastro_dicionario[nome][material] = quantidade
    cadastro_dicionario[nome]["extra"] = (nutricao,rendimento)
    return cadastro_dicionario


def json_stuff():
    try:
        with open("cadastro_intens.json", "r") as arquivo:
            cadastro_dicionario = json.load(arquivo)
            print(cadastro_dicionario)
    except (ValueError, FileNotFoundError):
        cadastro_dicionario = {}
    cadastro_dicionario = cadastro_itens(cadastro_dicionario)
    with open("cadastro_intens.json", "w") as arquivo:
        json.dump(cadastro_dicionario, arquivo, indent =4)
    return cadastro_dicionario
  




