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

    locais = []
    itens = []
    caminhoes = []

    while opcao:
        opcao = menu()
        if opcao == "0":
            # opcao = False
            print(entregas)

        elif opcao == "1":
            idLocal = input("Digite um identificador para o Local: ")
            nomeLocal = input("Digite um nome para o Local: ")
            local = Local(idLocal, nomeLocal, None, None)
            # entregas["Locais"].append(local.inserirLocal())
            locais.append(local.inserirLocal())
            print(locais)
            # print(entregas)

        elif opcao == "2":
            idItem = input("Digite um identificador para o Item: ")
            nomeItem = input("Digite um nome para o Item: ")
            item = ItemEntrega(idItem, nomeItem)
            # entregas["Itens"].append(item.addItem())
            itens.append(item.addItem())
            # print(entregas)
            print(itens)
            # sleep(1)

        elif opcao == "3":
            placa = input("Digite a placa do Caminhão: ")
            caminhao = Caminhao(placa, None, None, None, None)
            # entregas["Caminhao"].append(caminhao.inserirCaminhao())
            caminhoes.append(caminhao.inserirCaminhao())
            print(caminhoes)
            # print(entregas)

        elif opcao == "4":
            print("------------------------------------------")
            j = 0
            for i in itens:
                print("[" + str(j) + "]", "Id:" + i[0], "Nome: " + i[1])
                j += 1
            itemAs = input("Selecione um item para se associado: ")
            # print(entregas["Itens"].__getitem__(int(itemAs)))
            print(itens[int(itemAs)])

            j = 0
            print("------------------------------------------")
            for i in locais:
                print("[" + str(j) + "]", "Id:" + i[0], "Nome: " + i[1])
                j += 1
            localAs = input("Selecione um local para associar o item: ")
            # entregas["Locais"].__getitem__(int(localAs))
            print(locais[int(localAs)])

            for i in locais[int(localAs)]:
                nIdLocal = i[0]
                nNomeLcal = i[1]
            for i in itens[int(itemAs)]:
                nIdItem = i[0]
                nNomeItem = i[1]

            novoLocal = Local(nIdLocal,nNomeLcal,nIdItem,nNomeItem)
            entregas["Locais"].append(novoLocal.inserirLocal())

            itens.pop(int(itemAs))
            print(entregas)
            print(itens)

        elif opcao == "5":
            j = 0
            print("------------------------------------------")
            for i in locais:
                print("[" + str(j) + "]", "Id:" + i[0], "Nome: " + i[1])
                j += 1
            localAs = input("Selecione um local para associar a um caminhão: ")

            j = 0
            for i in caminhoes:
                print("[" + str(j) + "]", "Placa:" + i[0])
                j += 1
            caminhaoAs = input("Selecione o caminhão que será associado: ")

            for i in locais[int(localAs)]:
                nIdLocal = i[0]
                nNomeLcal = i[1]

            novoCaminhao = Caminhao()

        elif opcao == "6":

            pass



if __name__ == '__main__':
    main()
