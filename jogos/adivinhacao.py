import random

def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 100

    print("Numero secredto: {}".format(numero_secreto))

    print("*********************************")

    print("Qual nível de dificuldade?")
    print("1 - Fáciol | 2 - Média | 3 - Dificíl")

    nivel = int(input("Difina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 15
    else:
        total_de_tentativas = 10

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você chutou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("Você errou, seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou, seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if __name__ == "__main__":
    jogar_adivinhacao()