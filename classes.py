class ItemEntrega:

    def __init__(self, idItem, nomeItem):
        self.idItem = idItem
        self.nome = nomeItem

    def addItem(self):
        pass


class Local(ItemEntrega):

    def __init__(self, idLocal, nomeLocal, idItem, nomeItem):
        self.idLocal = idLocal
        self.nome = nomeLocal
        super().__init__(idItem,nomeItem)


class Caminhao(Local,ItemEntrega):

    def __init__(self, placa, nomeLocal, idLocal, idItem, nomeItem):
        self.placa = placa
        super().__init__(idLocal,nomeLocal)
        super().__init__(idItem, nomeItem)

    def info (self):
        print(self.placa)
        print(self.nome)
        print(self.nomeLocal)




