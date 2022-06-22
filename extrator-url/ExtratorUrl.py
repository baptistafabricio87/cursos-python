class ExtratorUrl:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        url = url.strip()
        return url

    def valida_url(self):
        if self.url == "":
            raise ValueError('A URL está vazia')
    
    def base_url(self, url):
        indice_interrogacao = url.find('?')
        url_base = url[:indice_interrogacao]
        return url_base

    def separa_url(self, url):
        indice_interrogacao = url.find('?')
        url_parametro = url[indice_interrogacao + 1]
        return url_parametro

    # def busca_parametro(self, url, parametro_busca):
    #     indice_parametro = self.url_parametro.find(parametro_busca)
    #     indice_valor = indice_parametro + len(parametro_busca) + 1
    #     indice_e_comercial = url_parametros.find('&', indice_valor)
    #     if indice_e_comercial == -1:
    #         valor = url_parametros[indice_valor:]
    #     else:
    #         valor = url_parametros[indice_valor:indice_e_comercial]


extrator_url = ExtratorUrl("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
print(extrator_url)
