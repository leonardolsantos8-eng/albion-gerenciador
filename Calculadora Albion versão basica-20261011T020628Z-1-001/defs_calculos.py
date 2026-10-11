import json
import defs_cadastro


def json_calculos():
    with open("cadastro_intens.json", "r") as arquivo:
        calculos_dicionario = json.load(arquivo)
    return calculos_dicionario


def inicio_calculos():
    calculos_dicionario = json_calculos()
    chave_dicionario = listar_dicionario(calculos_dicionario)
    valor_unitario, lista_chaves, nutricao_gasta, rendimento = valores_dicionario(chave_dicionario,calculos_dicionario)
    calculos_itens(valor_unitario,chave_dicionario,calculos_dicionario,lista_chaves,nutricao_gasta,rendimento)

def listar_dicionario(calculos_dicionario):
    lista = list(calculos_dicionario.keys())
    count = len(lista)
    for chave in range(count):
        porcao = lista[chave]
        print(f"{chave +1} - {porcao}")
    escolha = int(input("Informa opçao da porçao: "))
    escolha = escolha - 1
    chave_dicionario = lista[escolha]
    return chave_dicionario


def valores_dicionario(chave_dicionario,calculos_dicionario):
    valor_unitario = {}
    lista_chaves = list(calculos_dicionario[chave_dicionario].keys())
    for chave in lista_chaves:
        if chave == "extra":
            lista_extra =  calculos_dicionario[chave_dicionario][chave]
            nutricao_gasta = lista_extra[0]
            rendimento = lista_extra[1]
            break
        preco = float(input(f"Informe valor do material {chave}: "))
        valor_unitario[chave] = preco
    return valor_unitario, lista_chaves, nutricao_gasta, rendimento


def calculos_itens(valor_unitario,chave_dicionario,calculos_dicionario,lista_chaves,nutricao_gasta,rendimento):
    desconto = float(input("Informe valor do desconto: 15 | 20 | 25: "))
    desconto = (100 - desconto) / 100
    nutricao = int(input("Informe valor da nutriçao: "))
    total = 0
    for chave in lista_chaves:
        if chave == "extra":
            break
        valor = valor_unitario[chave]
        quantidade = calculos_dicionario[chave_dicionario][chave]
        resultado = valor * quantidade
        total +=  resultado
        print(resultado)
        print(total)

    print(total)
    total_final = total * desconto
    print(total_final)
    total_final += nutricao_gasta * (nutricao/100)
    print(total_final)
    total_final = total_final / rendimento
    print(total_final)















