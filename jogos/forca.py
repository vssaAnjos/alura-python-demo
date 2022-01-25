# forca.py
import random


def jogar():
    imprimir_mensagem_inicial()
    palavra_secreta = gerar_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    # Enquanto é True e True = não enforcou e não acertou
    while (not acertou and not enforcou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marcar_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1

        enforcou = (erros == 6)
        acertou = ("_" not in letras_acertadas)
        print(letras_acertadas)

    if (acertou):
        imprimir_mensagem_ganhador(palavra_secreta)
    else:
        imprimir_mensagem_perdedor()
    print("Fim do jogo")


def imprimir_mensagem_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def gerar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    print(palavras)

    numero_randomico = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_randomico].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()  # para limpar espaço em branco
    return chute


def marcar_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):  # .upper para comparar tudo como maiscula
            letras_acertadas[index] = letra
        index = index + 1


def imprimir_mensagem_ganhador(palavra_secreta):
    print("Você acertou! A palavra secreta é {}".format(palavra_secreta))


def imprimir_mensagem_perdedor():
    print("Você perdeu!")


if (__name__ == "__main__"):
    jogar()
