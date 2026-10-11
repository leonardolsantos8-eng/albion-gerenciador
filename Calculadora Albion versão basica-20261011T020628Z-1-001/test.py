# def iniciar_cadastro_itens():
#     cadastro_itens()



# def cadastro_itens():
#     nome = input("Informe nome do iten: ")
#     nutricao = float(input("Informe Nutriçao por porçao: "))
#     rendimento = int(input("Informe rendimento final: "))
#     #artefatos = input("Craft com artefatos? s|n: ")
#     componetes_itens(nome,nutricao,rendimento)



# def componetes_itens(nome,nutricao,rendimento):
#     cadastro_dicionario = {}
#     cadastro_dicionario[nome] = {}
#     while True:
#         material = input("Informe nome do material: 'sair' para sair: ")
#         if material == "sair":
#             break
#         quantidade = float(input("Informe quantidade do mateiral: "))
#         cadastro_dicionario[nome][material] = quantidade
#     cadastro_dicionario[nome]["extra"] = (nutricao,rendimento)
#     print(cadastro_dicionario)





# iniciar_cadastro_itens()

import json
import defs_cadastro



def json_calculos():
    with open("cadastro_intens.json", "r") as arquivo:
        calculos_dicionario = json.load(arquivo)
    return calculos_dicionario


def inicio_calculos():
    calculos_dicionario = json_calculos()
    escolha = listar_dicionario(calculos_dicionario)
    valor_unitario = valores_dicionario(escolha,calculos_dicionario)

def listar_dicionario(calculos_dicionario):
    lista = list(calculos_dicionario.keys())
    count = len(lista)
    for chave in range(count):
        porcao = lista[chave]
        print(f"{chave +1} - {porcao}")
    escolha = int(input("Informa opçao da porçao: "))
    return escolha


def valores_dicionario(escolha,calculos_dicionario):
    valor_unitario = {}
    lista_chaves = list(calculos_dicionario[escolha].keys())
    print(lista_chaves)
    for chave in lista_chaves:
        if chave == "extra":
            break
        preco = float(input(f"Informe valor do material {chave}: "))
        valor_unitario[chave] = preco
    desconto = float(input("Informe valor do desconto: 15 | 20 | 25 "))
    desconto = (100 - desconto) / 100
    valor_unitario["desconto"] = desconto
    nutricao = int(input("Informe valor da nutriçao: "))
    valor_unitario["nutriçao"] = nutricao
    print(valor_unitario)
    return valor_unitario



def calculos_itens(valor_unitario,chave_dicionario):
    










inicio_calculos()

