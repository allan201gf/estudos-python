print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 43
total_de_tentativas = 5
rodada = 1

while rodada <= total_de_tentativas:
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você chutou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou")
    else:
        if maior:
            print("Você errou, seu chute foi maior que o número secreto.")
        elif menor:
            print("Você errou, seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")