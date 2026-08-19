from heroi import Cavaleiro, Mago
from inimigo import Inimigo
from batalha import batalhar


print("=== Bem-vindo ao meu RPG ===")

while True:
    nome = input("Digite seu nome: ").strip()

    if nome:
        break

    print("❌ O nome não pode ficar vazio!")
    print()


print()
print("Escolha sua classe:")
print("1 - ⚔️  Cavaleiro  (Vida: 120 | Ataque: 20 | Mana: 30)")
print("2 - 🔮 Mago        (Vida: 70  | Ataque: 10 | Mana: 100)")
print()

while True:
    escolha = input("Digite 1 ou 2: ").strip()

    if escolha == "1":
        heroi = Cavaleiro(nome)
        break

    elif escolha == "2":
        heroi = Mago(nome)
        break

    else:
        print("❌ Opção inválida! Digite apenas 1 ou 2.")
        print()


print()
print(f"{heroi.__class__.__name__} '{heroi.nome}' criado com sucesso!")
heroi.mostrar_status()


print()
print("=== VOCÊ ENTRA NA DUNGEON ===")
print()
print("O corredor está escuro e úmido...")
print("De repente, um inimigo aparece na sua frente!")
print()

inimigo = Inimigo(
    nome="Goblin",
    vida=50,
    ataque_min=5,
    ataque_max=15
)

print(f"💀 {inimigo.nome} apareceu!")
print(f"❤️ Vida do inimigo: {inimigo.vida}")
print(f"⚔️ Ataque do inimigo: {inimigo.ataque}")

print()

batalhar(heroi, inimigo)
