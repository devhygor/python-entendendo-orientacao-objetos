#encoding utf-8


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self._likes} Likes')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes')


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes')


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return(len(self.programas))

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('Playlist fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana.programas:
    print(programa)
