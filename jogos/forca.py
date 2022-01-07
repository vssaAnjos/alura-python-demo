# forca.py
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    # Enquanto é True e True = não enforcou e não acertou
    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip() # para limpar espaço em branco
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):    # .upper para comparar tudo como maiscula
                print("Encontrei a letra {} na posição {}".format(letra,index))
                index = index + 1
        else:
            print("Não encontrado...")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
