from classes import *

def menu():
    print("------------------------------------------")
    print("[1] Inserir ponto de entrega")
    print("[2] Inserir item de entrega")
    print("[3] Inserir caminhão")
    print("[4] Associar item a ponto de entrega")
    print("[5] Associar ponto de entrega a caminhão")
    print("[6] Realizar entregas")
    print("[0] Sair")
    opcao = input()
    return opcao

opcao = True

while opcao:
    opcao = menu()
    if opcao == "0":
        opcao = False
