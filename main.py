class Item:
    def __init__(self, tipo: str, efeito: int):
        self.tipo = tipo
        self.efeito = efeito

class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: Item):
        if not item:
            print("Escolha um item para inserir")
            return
        self.itens.append(item)

    def listar_itens(self):
        for item in self.itens:
            print(f"Item: {item.tipo}, Efeito: {item.efeito}")

class Player:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.vivo = True
        self.inventario = Inventario()

    def usar_pocao(self, pocao):
        if not self.vivo:
            print("Game over!")
            return

        efeito_pocao = pocao.usar()
        nova_energia = self.energia + efeito_pocao

        if nova_energia <= 0:
            nova_energia = 0
            self.vivo = False

        if nova_energia >= 100:
            nova_energia = 100
            print("Impossível usar cura!")

        self.energia = nova_energia
        self.status()

    def status(self):
        print(f"\n------- STATUS ---------")
        print(f"Vivo: {self.vivo} - Energia: {self.energia}%")
        print(f"------------------------\n")

class PocaoVerde:
    def __init__(self, tipo: str, efeito: int):
        self.tipo = tipo
        self.efeito = efeito

    def usar(self):
        return self.efeito

class PocaoRoxa:
    def __init__(self, tipo: str, efeito: int):
        self.tipo = tipo
        self.efeito = efeito

    def usar(self):
        return -self.efeito

# Testando o sistema
p1 = Player("Kronus")

# Criando poções
cura = PocaoVerde("Cura Verde", 15)
veneno = PocaoRoxa("Morte Certa", 25)

# Adicionando itens ao inventário do player
faca = Item("Faca Tramontina", 120)
escudo = Item("Escudo do Rei", 50)

p1.inventario.adicionar_item(faca)
p1.inventario.adicionar_item(escudo)

# Mostrando inventário
p1.inventario.listar_itens()

# Usando poções
p1.usar_pocao(cura)
p1.usar_pocao(veneno)

# Mostrando status final
p1.status()
