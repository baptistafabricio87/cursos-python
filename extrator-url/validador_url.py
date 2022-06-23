import re

url = 'https://www.bytebank.com.br/cambio'

padrao = '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio'
url_padrao = re.compile(padrao)
match = url_padrao.match(url)

if not match:
    raise ValueError('URL inválida')

print('URL válida')