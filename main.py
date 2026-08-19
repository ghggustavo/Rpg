from heroi import Heroi
from inimigo import Inimigo
from batalha import batalhar
from loja import abrir_loja

print( "=== Bem-vindo ao meu RPG === ")
nome= input ("Digite seu nome: ")

print()
print("Escolha sua classe:")
print("1 - ⚔️  Cavaleiro  (Vida: 120 | Ataque: 20 | Mana: 30)")
print("2 - 🔮 Mago        (Vida: 70  | Ataque: 10 | Mana: 100)")
print()

while True:
    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        classe = "Cavaleiro"
        vida = 120
        ataque = 20
        mana = 30
        ouro = 0
        break
    elif escolha == "2":
        classe = "Mago"
        vida = 70
        ataque = 10
        mana = 100
        ouro = 0
        break
    else:
        print("❌ Opção inválida! Digite apenas 1 ou 2.")
        print()

print()
print(f"Herói '{nome}' o {classe} criado com sucesso!")
print(f"❤️  Vida:   {vida}")
print(f"⚔️  Ataque: {ataque}")
print(f"💙 Mana:   {mana}")