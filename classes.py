class ItemEntrega:

    def __init__(self, idItem, nomeItem):
        self.idItem = idItem
        self.nomeItem = nomeItem

    def addItem(self):
        return self.idItem, self.nomeItem


class Local(ItemEntrega):

    def __init__(self, idLocal, nomeLocal, idItem, nomeItem):
        self.idLocal = idLocal
        self.nomeLocal = nomeLocal
        super().__init__(idItem, nomeItem)

    def inserirLocal(self):
        return self.idLocal, self.nomeLocal, self.nomeItem


class Caminhao(Local):

    def __init__(self, placa, idLocal, nomeLocal, idItem, nomeItem):
        self.placa = placa
        super().__init__(idLocal, nomeLocal, idItem, nomeItem)

    def inserirCaminhao(self):
        return self.placa, self.nomeLocal, self.nomeItem
