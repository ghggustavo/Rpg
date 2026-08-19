from personagem import Personagem
import random


class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque_min, ataque_max):
        ataque = random.randint(ataque_min, ataque_max)

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