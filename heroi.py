from personagem import Personagem

class Heroi(Personagem):
    def __init__(self, nome, classe, vida, ataque, mana):
        super().__init__(nome, vida, ataque, mana)
        self.classe = classe
        self.ouro = 0