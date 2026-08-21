from personagem import Personagem
import random


class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, mana):
        super().__init__(nome, vida, ataque, mana)
        self.ouro = 0

    def mostrar_status(self):
        print(f"❤️  Vida:   {self.vida}")
        print(f"⚔️  Ataque: {self.ataque}")
        print(f"💙 Mana:    {self.mana}")
        print(f"💰 Ouro:    {self.ouro}")

    def mostrar_acoes(self):
        print("1 - ⚔️  Atacar")
        print("2 - 🏃 Fugir")

    def executar_acao(self, acao, inimigo):
        if acao == "1":
            return self.atacar(inimigo)

        return None


class Cavaleiro(Heroi):
    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=120,
            ataque=20,
            mana=30
        )
        self.defendendo = False

    def mostrar_acoes(self):
        print("1 - ⚔️  Atacar")
        print("2 - 🛡️  Defender")
        print("3 - ⚡ Ataque Duplo")
        print("4 - 🏃 Fugir")

    def executar_acao(self, acao, inimigo):

        if acao == "1":
            return self.atacar(inimigo)

        elif acao == "2":
            return self.defender()

        elif acao == "3":
            return self.ataque_duplo(inimigo)

        return None

    def atacar(self, inimigo):
        dano = random.randint(
            self.ataque - 5,
            self.ataque + 5
        )

        inimigo.receber_dano(dano)

        print(
            f"⚔️ Você atacou o {inimigo.nome} "
            f"e causou {dano} de dano!"
        )

        return True

    def defender(self):
        self.defendendo = True
        print("🛡️ Você assumiu postura defensiva!")
        return True

    def ataque_duplo(self, inimigo):

        if self.vida <= 20:
            print("❌ Vida insuficiente para o ataque duplo!")
            return False

        dano1 = random.randint(
            self.ataque - 5,
            self.ataque + 5
        )

        dano2 = random.randint(
            self.ataque - 5,
            self.ataque + 5
        )

        self.vida -= 20

        inimigo.receber_dano(dano1)
        inimigo.receber_dano(dano2)

        print("⚡ ATAQUE DUPLO!")
        print(f"💥 Primeiro golpe: {dano1}")
        print(f"💥 Segundo golpe: {dano2}")
        print(f"💥 Dano total: {dano1 + dano2}!")
        print("❤️ Você perdeu 20 de vida no esforço.")

        return True


class Mago(Heroi):
    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=70,
            ataque=10,
            mana=100
        )

        self.ataque_magico = 20
        self.escudo_ativo = False

    def mostrar_acoes(self):
        print("1 - ⚔️  Atacar")
        print("2 - 💥 Magia Especial")
        print("3 - 🛡️  Escudo Mágico")
        print("4 - 🏃 Fugir")

    def executar_acao(self, acao, inimigo):

        if acao == "1":
            return self.atacar(inimigo)

        elif acao == "2":
            return self.magia_especial(inimigo)

        elif acao == "3":
            return self.escudo_magico()

        return None

    def atacar(self, inimigo):
        if self.mana < 15:
            print("💙 Você não tem mana suficiente para atacar!")
            return False

        dano = random.randint(
            self.ataque_magico - 3,
            self.ataque_magico + 8
        )

        self.mana -= 15

        inimigo.receber_dano(dano)

        print(
            f"🔮 Você lançou uma magia e causou "
            f"{dano} de dano!"
        )

        print(f"💙 Mana restante: {self.mana}")

        return True

    def magia_especial(self, inimigo):

        if self.mana <30:
            print("❌ Mana insuficiente para a magia especial!")
            return False

        dano = random.randint(
                self.ataque_magico + 10,
                self.ataque_magico + 25
        )

        self.mana -= 30

        inimigo.receber_dano(dano)

        print("💥 MAGIA ESPECIAL!")
        print(f"🔮 Você causou {dano} de dano!")
        print(f"💙 Mana restante: {self.mana}")

        return True

    def escudo_magico(self):

        if self.mana < 25:
            print("❌ Mana insuficiente para ativar o escudo!")
            return False

        self.mana -= 25
        self.escudo_ativo = True

        print("🛡️ ESCUDO MÁGICO!")
        print("✨ O próximo ataque recebido terá o dano reduzido!")
        print(f"💙 Mana restante: {self.mana}")

        return True

    def receber_dano(self, dano):

        if self.escudo_ativo:
            dano = dano // 2
            self.escudo_ativo = False

            print("🛡️ O escudo mágico reduziu o dano pela metade!")

        super().receber_dano(dano)