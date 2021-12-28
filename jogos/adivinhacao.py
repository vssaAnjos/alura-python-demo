# adivinhacao.py

import random


def jogar():
    print("***********************************")
    print("Bem vindo ao Jogo de Adivinhação!")
    print("***********************************")

    # Init var
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    rodada = 1
    pontos = 1000
    # To define level
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defini o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # Validate round
    print(numero_secreto)
    for rodada in range(1, total_de_tentativas + 1):
        # print("Tentativa ",rodada,"de",total_de_tentativas)
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou! e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! Seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! Seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)  # pontos perdidos da rodada
            pontos = pontos - pontos_perdidos  # Subtraindo pontos perdidos da pontuação total
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

    print("Fim de jogo!")
