arquivo = open("../jogos/palavras.txt", "w")

arquivo.write("banana\n")
arquivo.write("melancia\n")

arquivo.close()

arquivo = open("../jogos/palavras.txt", "a")
arquivo.write("morango\n")
arquivo.write("maça\n")

arquivo.close()

arquivo = open("../jogos/palavras.txt", "r")

for linha in arquivo:
    print(linha.strip())