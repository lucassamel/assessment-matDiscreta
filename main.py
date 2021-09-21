from time import sleep

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


def main():
    opcao = True

    entregas = {"Locais": [],
                "Itens": [],
                "Caminhao": []}

    while opcao:
        opcao = menu()
        if opcao == "0":
            opcao = False

        elif opcao == "1":
            idLocal = input("Digite um identificador para o Local: ")
            nomeLocal = input("Digite um nome para o Local: ")
            local = Local(idLocal, nomeLocal, None, None)
            entregas["Locais"].append(local.inserirLocal())
            print(entregas)

        elif opcao == "2":
            idItem = input("Digite um identificador para o Item: ")
            nomeItem = input("Digite um nome para o Item: ")
            item = ItemEntrega(idItem, nomeItem)
            entregas["Itens"].append(item.addItem())
            print(entregas)
            sleep(1)

        elif opcao == "3":
            placa = input("Digite a placa do Caminhão: ")
            caminhao = Caminhao(placa, None, None, None, None)
            entregas["Caminhao"].append(caminhao.inserirCaminhao())
            print(entregas)

        elif opcao == "4":
            j = 0
            for i in entregas["Itens"]:
                print("[" + str(j) + "]", "Id:" + i[0], "Nome: " + i[1])
                j += 1
            itemAss = input("Selecione um item para se associado: ")
            j = 0
            for i  in entregas["Locais"]:
                print()


        elif opcao == "5":

            pass
        elif opcao == "6":

            pass


if __name__ == '__main__':
    main()
