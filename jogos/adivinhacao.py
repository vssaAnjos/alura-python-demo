print("***********************************")
print("Bem vindo ao Jogo de Adivinhação!")
print("***********************************")

numero_secreto=42
total_de_tentativas=3
rodada=1
while(rodada <= total_de_tentativas):
    print("Tentativa ",rodada,"de",total_de_tentativas)
    chute_str= input("DIGITE SEU NUMERO: ")

    print("Você digitou: ", chute_str)

    chute = int(chute_str)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o numero")
        elif(menor):
            print("Você errou! Seu chute foi menor que o numero")
    rodada=rodada + 1
print("Fim de jogo!")