class Personagem:
    def __init__(self, nome, vida, ataque, mana=0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.mana = mana


    def receber_dano(self, dano):
        self.vida -= dano


    def esta_vivo(self):
        return self.vida > 0