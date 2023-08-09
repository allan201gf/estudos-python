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

onzeHomens = Filme("Onze Homens e Um Segredo", 2010, 200)
onzeHomens.dar_likes()
onzeHomens.dar_likes()
onzeHomens.dar_likes()


demolidor = Serie("Demolidor", 2000, 100)
demolidor.dar_likes()

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome;
        self._programas = programas

    @property
    def listagem(self):
            return self._programas
        
    @property
    def tamanho(self):
            return len(self._programas)

    def __getitem__(self, item):
        return self._programas[item]


filmes_e_series = [vingadores, atlanta, onzeHomens, demolidor]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana.listagem)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Ta ou nao ta? {demolidor in playlist_fim_de_semana}')