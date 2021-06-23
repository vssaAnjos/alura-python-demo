print("***********************************")
print("Bem vindo ao Jogo de Adivinhação!")
print("***********************************")

numero_secreto=42
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

print("Fim de jogo!")