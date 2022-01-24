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
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()  # para limpar espaço em branco

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):  # .upper para comparar tudo como maiscula
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros += 1

        enforcou = (erros == 6)
        acertou = ("_" not in letras_acertadas)
        print(letras_acertadas)

    if (acertou):
        print("Você acertou! A palavra secreta é {}".format(palavra_secreta))
    else:
        print("Você perdeu!")
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


if (__name__ == "__main__"):
    jogar()
