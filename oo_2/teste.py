from modelo import Filme, Serie

filme = Filme('vingadores - guerra givil', 2018, 160)
filme.likes = 1
filme.likes = 1
print(f'Nome: {filme.nome} - Ano: {filme.ano} - Duracao: {filme.duracao} - Likes: {filme.likes}')

serie = Serie('atlanta', 2018, 2)
serie.likes = 1
serie.likes = 1
serie.likes = 1
print(f'Nome: {serie.nome} - Ano: {serie.ano} - Temporadas: {serie.temporadas} - Likes: {serie.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.nome = 'atlanta - de glover'
atlanta.likes = 2
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')