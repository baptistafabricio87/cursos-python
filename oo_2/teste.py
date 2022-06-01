from modelo import Filme, Serie, Playlist

avenger = Filme('vingadores - guerra inifita', 2018, 160)
tmep = Filme('todo mundo em panico - guerra inifita', 1999, 90)
atlanta = Serie('atlanta - de glover', 2018, 4)
demolidor = Serie('demolidor', 2016, 8)
avenger.dar_likes()
avenger.dar_likes()
avenger.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
atlanta.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

filmes_series = [atlanta, tmep, avenger, demolidor]
playlist_fim_de_semana = Playlist('fim de semana', filmes_series)

print('Tamanho da Playlist: ', len(playlist_fim_de_semana))
for programa in playlist_fim_de_semana:
    print(programa)

print('Tá ou não Tá? ', demolidor in  playlist_fim_de_semana)