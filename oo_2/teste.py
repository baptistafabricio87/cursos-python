from modelo import Filme, Serie

filme = Filme('vingadores - guerra inifita', 2018, 160)
serie = Serie('atlanta - de glover', 2018, 2)

filmes_series = [filme, serie]

for programa in filmes_series:
    programa.imprime()





# filme.dar_likes()
# print(f'Nome: {filme.nome} - Likes: {filme.likes}')

# serie.dar_likes()
# print(f'Nome: {serie.nome} - Likes: {serie.likes}')

# atlanta.dar_likes()
# print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')