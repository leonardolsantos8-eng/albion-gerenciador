import defs_cadastro as defs
import json
import defs_calculos as calculos
from tkinter import *



#calculadora Albion

print("Calculadora Albion")
while True:
    print("Menu principal")
    print("1 - Cadastro de itens. " \
    "2 - Calculos Valores. ")
    opcao = input("Informe opção: ")
    match opcao:
        case "1":
            defs.iniciar_cadastro_itens()

        case "2":
            calculos.inicio_calculos()

        




