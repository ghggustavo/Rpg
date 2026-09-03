from personagem import Personagem
import random


class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque_min, ataque_max):

        self.ataque_min = ataque_min
        self.ataque_max = ataque_max

        ataque = random.randint(
            self.ataque_min,
            self.ataque_max
        )

        super().__init__(
            nome=nome,
            vida=vida,
            ataque=ataque
        )

    def calcular_dano(self):
        return random.randint(
            self.ataque - 3,
            self.ataque + 3
        )

    def atacar(self, personagem):
        dano = self.calcular_dano()

        personagem.receber_dano(dano)

        print(
            f"💀 O {self.nome} contra-atacou "
            f"e causou {dano} de dano!"
        )

class Goblin(Inimigo):
    def __init__(self):
        super().__init__(
            nome="Goblin",
            vida=50,
            ataque_min=8,
            ataque_max=12
        )

class Orc(Inimigo):
    def __init__(self):
        super().__init__(
            nome="Orc",
            vida=80,
            ataque_min=12,
            ataque_max=20
        )

    def calcular_dano(self):
        if random.random() < 0.25:
            print("💥 O Orc desferiu um Golpe Brutal!")
            return self.ataque_max

        return super().calcular_dano()