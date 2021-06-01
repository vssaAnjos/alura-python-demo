print("***********************************")
print("Bem vindo ao Jogo de Adivinhação!")
print("***********************************")

numero_secreto=42
chute_str= input("DIGITE SEU NUMERO: ")

print("Você digitou: ", chute_str)

chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")