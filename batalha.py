import random


def batalhar(heroi, inimigo):

    while heroi.esta_vivo() and inimigo.esta_vivo():

        print("O que você quer fazer?")
        heroi.mostrar_acoes()
        print()

        acao = input("Digite sua ação: ").strip()

        if acao == "4":
            print("🏃 Você fugiu da batalha!")
            return False

        acao_realizada = heroi.executar_acao(acao, inimigo)

        if acao_realizada is None:
            print("❌ Opção inválida!")
            continue

        if not acao_realizada:
            continue

        if inimigo.esta_vivo():

            dano = inimigo.calcular_dano()

            if hasattr(heroi, "defendendo") and heroi.defendendo:

                dano_reduzido = dano // 2

                heroi.receber_dano(dano_reduzido)

                print(
                    f"🛡️ Defesa ativada! "
                    f"O dano foi reduzido de {dano} "
                    f"para {dano_reduzido}!"
                )

                heroi.defendendo = False

            else:
                heroi.receber_dano(dano)

                print(
                    f"💀 O {inimigo.nome} contra-atacou "
                    f"e causou {dano} de dano!"
                )

        print()
        print(
            f"❤️ Sua vida: {max(0, heroi.vida)}"
            f" | ❤️ Vida do {inimigo.nome}: "
            f"{max(0, inimigo.vida)}"
        )
        print()

    # Resultado da batalha

    if not inimigo.esta_vivo():

        ouro_ganho = random.randint(10, 15)
        heroi.ouro += ouro_ganho

        print(f"🏆 Você derrotou o {inimigo.nome}!")
        print(
            f"💰 Você ganhou {ouro_ganho} de ouro! "
            f"Total: {heroi.ouro}"
        )

        return True

    if not heroi.esta_vivo():

        print("💀 Você foi derrotado... Game Over!")
        return False