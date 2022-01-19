# forca.py
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
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
        print("Você acertou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
