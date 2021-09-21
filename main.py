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
                "Caminhao": []}

    locais = [("001", "niteroi"), ("002", "rio de janeiro")]
    itens = [("001", "iphone"), ("002", "televisao"), ("003", "sofá")]
    caminhoes = ["PLACA 001", "PLACA 002"]

    while opcao:
        opcao = menu()
        if opcao == "0":
            # opcao = False
            print(entregas)

        elif opcao == "1":
            idLocal = input("Digite um identificador para o Local: ")
            nomeLocal = input("Digite um nome para o Local: ")
            local = Local(idLocal, nomeLocal, None, None)
            locais.append(local.inserirLocal())

        elif opcao == "2":
            idItem = input("Digite um identificador para o Item: ")
            nomeItem = input("Digite um nome para o Item: ")
            item = ItemEntrega(idItem, nomeItem)
            itens.append(item.addItem())

        elif opcao == "3":
            placa = input("Digite a placa do Caminhão: ")
            caminhao = Caminhao(placa, None, None, None, None)
            caminhoes.append(caminhao.inserirCaminhao())

        elif opcao == "4":
            print("------------------------------------------")
            j = 0
            for i in itens:
                print("[" + str(j) + "]", "Id:" + i[0], "Nome: " + i[1])
                j += 1
            itemAs = input("Selecione um item para se associado: ")

            j = 0
            print("------------------------------------------")
            for i in locais:
                print("[" + str(j) + "]", "Id:" + i[0], "Nome: " + i[1])
                j += 1
            localAs = input("Selecione um local para associar o item: ")

            iL = locais[int(localAs)]

            nIdLocal = iL[0]
            nNomeLocal = iL[1]

            iI = itens[int(itemAs)]
            nIdItem = iI[0]
            nNomeItem = iI[1]

            novoLocal = Local(nIdLocal, nNomeLocal, nIdItem, nNomeItem)
            entregas["Locais"].append(novoLocal.inserirLocal())

            itens.pop(int(itemAs))

        elif opcao == "5":
            j = 0
            print("------------------------------------------")
            for i in entregas["Locais"]:
                print("[" + str(j) + "]", "Id:" + i[0], "Nome: " + i[1])
                j += 1
            localAs = input("Selecione um local para associar a um caminhão: ")

            j = 0
            for i in caminhoes:
                print("[" + str(j) + "]", "Placa:" + i)
                j += 1
            caminhaoAs = input("Selecione o caminhão que será associado: ")

            iL = entregas["Locais"][int(localAs)]

            nIdLocal = iL[0]
            nNomeLocal = iL[1]
            nNomeItem = iL[2]

            iC = caminhoes[int(caminhaoAs)]
            nPlaca = iC

            novoCaminhao = Caminhao(nPlaca, nIdLocal, nNomeLocal, None, nNomeItem)

            entregas["Caminhao"].append(novoCaminhao.inserirCaminhao())
            # locais.pop(int(localAs))
            print(entregas)

        elif opcao == "6":

            for i in entregas["Caminhao"]:
                print("Percurso do caminhão ", i[0], " Foram entregues os itens:")
                for j in entregas["Caminhao"]:
                    if j[0] == i[0]:
                        print("Item: ", j[2], "Local: ", j[1])
                print("<---------------------->")

            print("Total de pontos de entrega: ", str(len(locais)))
            print("Total de itens entregues: ", )

if __name__ == '__main__':
    main()
