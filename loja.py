def abrir_loja(heroi):
    
    print()
    print("=== VOCÊ ENCONTROU UMA LOJA ===")
    print()
    print(f"💰 Ouro disponível: {heroi.ouro}")
    print()
    print("O que deseja comprar?")
    print("1 - 🧪 Poção de Vida     (+30 vida)   | Custo: 10 ouro")

    if heroi.classe == "Mago":
        print("2 - 💧 Poção de Mana     (+40 mana)   | Custo: 10 ouro")
    else:
        print("2 - 🛡️  Escudo reforçado  (+10 ataque) | Custo: 15 ouro")

    print("3 - 🚪 Sair da loja")
    print()

    while True:
        compra = input("Digite 1, 2 ou 3: ")

        if compra == "1":
            if heroi.ouro >= 10:
                heroi.vida = heroi.vida + 30
                heroi.ouro = heroi.ouro - 10
                print(f"🧪 Você bebeu a poção! ❤️  Vida: {heroi.vida} | 💰 Ouro: {heroi.ouro}")
            else:
                print("❌ Ouro insuficiente!")

        elif compra == "2":
            if heroi.classe == "Mago":
                if heroi.ouro >= 10:
                    heroi.mana = heroi.mana + 40
                    heroi.ouro = heroi.ouro - 10
                    print(f"💧 Mana restaurada! 💙 Mana: {heroi.mana} | 💰 Ouro: {heroi.ouro}")
                else:
                    print("❌ Ouro insuficiente!")
            else:
                if heroi.ouro >= 15:
                    heroi.ataque = heroi.ataque + 10
                    heroi.ouro = heroi.ouro - 15
                    print(f"🛡️  Escudo equipado! ⚔️  Ataque: {heroi.ataque} | 💰 Ouro: {heroi.ouro}")
                else:
                    print("❌ Ouro insuficiente!")

        elif compra == "3":
            print("🚪 Você saiu da loja. Boa sorte, aventureiro!")
            break

        else:
            print("❌ Opção inválida!")

        print()

    # Status final
    print()
    print("=== STATUS FINAL ===")
    print(f"🧙 Herói:   {heroi.nome} o {heroi.classe}")
    print(f"❤️  Vida:    {heroi.vida}")
    print(f"⚔️  Ataque:  {heroi.ataque}")
    print(f"💙 Mana:    {heroi.mana}")
    print(f"💰 Ouro:    {heroi.ouro}")
