def batalhar(heroi, inimigo):

while monstro1_vida > 0 and vida > 0:
    print("O que você quer fazer?")
    print("1 - ⚔️  Atacar")
    print("2 - 🏃 Fugir")
    print()

    acao = input("Digite 1 ou 2: ")

    if acao == "1":
        if classe == "Mago":
            if mana <= 0:
                print("💙 Você não tem mana suficiente para atacar!")
                continue

            dano_jogador = random.randint(ataque - 3, ataque + 8)
            mana = mana - 15
            print(f"🔮 Você lançou uma magia e causou {dano_jogador} de dano!")
            print(f"💙 Mana restante: {mana}")

        else:  # Cavaleiro
            dano_jogador = random.randint(ataque - 5, ataque + 5)
            print(f"⚔️  Você atacou o {monstro1_nome} e causou {dano_jogador} de dano!")

        monstro1_vida = monstro1_vida - dano_jogador

        # Monstro contra-ataca (se ainda estiver vivo)
        if monstro1_vida > 0:
            dano_monstro = random.randint(monstro1_ataque - 3, monstro1_ataque + 3)
            vida = vida - dano_monstro
            print(f"💀 O {monstro1_nome} contra-atacou e causou {dano_monstro} de dano!")

    elif acao == "2":
        print("🏃 Você fugiu da batalha!")
        break

    else:
        print("❌ Opção inválida!")
        continue

    # Status após cada rodada
    print()
    if classe == "Mago":
        print(f"❤️  Sua vida: {vida}  |  💙 Mana: {mana}  |  ❤️  Vida do {monstro1_nome}: {max(0, monstro1_vida)}")
    else:
        print(f"❤️  Sua vida: {vida}  |  ❤️  Vida do {monstro1_nome}: {max(0, monstro1_vida)}")
    print()

# Resultado da batalha
if monstro1_vida <= 0:
    ouro_ganho = random.randint(10, 15)
    ouro = ouro + ouro_ganho
    print(f"🏆 Você derrotou o {monstro1_nome}!")
    print(f"💰 Você ganhou {ouro_ganho} de ouro! Total: {ouro}")
elif vida <= 0:
    print("💀 Você foi derrotado... Game Over!")