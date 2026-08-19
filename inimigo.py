from personagem import Personagem
import random

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque_min, ataque_max):
        ataque = random.randint(ataque_min, ataque_max)
        super().__init__(nome, vida, ataque)