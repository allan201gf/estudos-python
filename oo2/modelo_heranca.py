class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1   

    def __str__(self):
        return f'{self._nome} - Likes: {self._likes} - Ano: {self.ano}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - Likes: {self._likes} - Ano: {self.ano} - Duracao: {self.duracao}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - Likes: {self._likes} - Ano: {self.ano} - Temporadas: {self.temporadas}'

vingadores = Filme("Vingadores guerra infinita", 2018, 160)
vingadores.dar_likes()
# print(f'{vingadores.nome} - Likes: {vingadores.likes}')

atlanta = Serie("Atlanta", 2017, 2)
# print(atlanta.nome)

filmes_e_series = [vingadores, atlanta]
for programa in filmes_e_series:
    print(programa)
