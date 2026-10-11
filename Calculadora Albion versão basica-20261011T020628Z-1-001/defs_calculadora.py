import json





def iniciar_cadastro_itens():
    cadastro_itens()



def cadastro_itens():
    cadastro_dicionario = {}
    nome = input("Informe nome do inten")
    nutricao = float(input("Informe Nutriçao por porçao: "))
    rendimento = int(input("Informe rendimento final: "))
    #artefatos = input("Craft com artefatos? s|n: ")
    componetes_itens(nome,nutricao,rendimento)



def componetes_itens(nome,nutricao,rendimento):
    material = input("Informe nome do material: ")
    quantidade = float(input("Informe quantidade do mateiral: "))

    # try:
    #     with open("cadastro_itens.json", "r") as arquivo:
    #         itens_cadastrados = json.load(arquivo)
    # except ValueError,FileNotFoundError:
    #     pass
















