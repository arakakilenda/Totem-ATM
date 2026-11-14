"""
Jogo dos Três Copos
Programação de Computadores - Atividade A2.3 (Entrega 02)

O usuário escolhe um valor secreto, o programa o "esconde" em um de três
copos (C1, C2 ou C3) e o jogador tenta adivinhar em qual copo ele está.

Bibliotecas utilizadas:
    random -> sorteia em qual copo o valor ficará escondido
    time   -> cria pausas para simular o embaralhamento
"""

import random
import time

COPOS = ["C1", "C2", "C3"]


def exibir_boas_vindas():
    """Mostra o título do jogo e apresenta os copos."""
    print("=" * 40)
    print("   BEM-VINDO AO JOGO DOS TRÊS COPOS")
    print("=" * 40)
    print()
    print("Temos 3 copos na mesa: C1, C2 e C3.")


def ler_valor_secreto():
    """Pede o valor a ser escondido, repetindo até que não seja vazio."""
    while True:
        valor = input("Escolha um número qualquer para escondermos: ").strip()
        if valor:
            return valor
        print("Valor inválido! Digite algo para esconder.\n")


def embaralhar():
    """Simula o embaralhamento com mensagens e pausas dramáticas."""
    print("\nEscondendo o número e embaralhando os copos...")
    time.sleep(1)
    print("Embaralhando mais um pouco...")
    time.sleep(1)
    print("Pronto!\n")


def ler_palpite():
    """Lê o palpite do jogador e valida (aceita C1, C2 ou C3, em qualquer caixa)."""
    while True:
        palpite = input(
            "Em qual copo você acha que o número está? (Digite C1, C2 ou C3): "
        ).strip().upper()
        if palpite in COPOS:
            return palpite
        print("Entrada inválida! Digite apenas C1, C2 ou C3.\n")


def exibir_resultado(valor, copo_premiado, palpite):
    """Informa se o jogador acertou e mostra a situação final dos copos."""
    print("\n" + "-" * 40)
    print("             RESULTADO")
    print("-" * 40 + "\n")

    if palpite == copo_premiado:
        print("🎉 PARABÉNS! Você acertou em cheio!")
        print(f"O número {valor} realmente estava escondido no copo {copo_premiado}.")
    else:
        print("😕 Que pena, você errou!")
        print(f"Você escolheu {palpite}, mas o número {valor} estava no copo {copo_premiado}.")

    print("\nSituação final dos copos na mesa:")
    for copo in COPOS:
        conteudo = valor if copo == copo_premiado else "Vazio"
        print(f"{copo}: {conteudo}")


def jogar_novamente():
    """Pergunta se o jogador quer outra rodada (aceita apenas S ou N)."""
    while True:
        resposta = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
        if resposta in ("S", "N"):
            return resposta == "S"
        print("Entrada inválida! Digite S para sim ou N para não.")


def main():
    """Controla o fluxo do jogo: cada volta do laço é uma rodada."""
    jogando = True
    while jogando:
        exibir_boas_vindas()
        valor = ler_valor_secreto()

        # Sorteio da posição
        copo_premiado = random.choice(COPOS)

        embaralhar()
        palpite = ler_palpite()
        exibir_resultado(valor, copo_premiado, palpite)

        jogando = jogar_novamente()
        print()

    print("Obrigado por jogar! Até a próxima.")


if __name__ == "__main__":
    main()
