# forca.py
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou = False

    print(letras_acertadas)

    # Enquanto é True e True = não enforcou e não acertou
    while (not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip() # para limpar espaço em branco

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):    # .upper para comparar tudo como maiscula
              #  print("Encontrei a letra {} na posição {}".format(letra, index))
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)


    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
