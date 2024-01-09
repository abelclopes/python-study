class Pedido:
    def __init__(self, id: int, items: list, status: str):
        self.id = id
        self.items = items
        self.status = status

class Item:
    def __init__(self, id: int, nome: str, preco: float):
        self.id = id
        self.nome = nome
        self.preco = preco

class Usuario:
    def __init__(self, id: int, nome: str, pedidos: list):
        self.id = id
        self.nome = nome
        self.pedidos = pedidos
