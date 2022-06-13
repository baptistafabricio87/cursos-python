url="bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao + 1:]
index_e = url_parametros.find('&')
url_param_1 = url_parametros[:index_e]

print(url_parametros)
print(url_param_1)
