import re

class ExtratorUrl:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao = '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio'
        url_padrao = re.compile(padrao)
        match = url_padrao.match(self.url)
        if not match:
            raise ValueError('URL Inválida')
    
    def get_base_url(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametro = self.url[indice_interrogacao + 1:]
        return url_parametro

    def busca_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
    
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self) -> str:
        return self.url

    def __eq__(self, other) -> bool:
        return self.url == other.url


extrator = ExtratorUrl("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
extrator2 = ExtratorUrl("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
# extrator = ExtratorUrl("bytebank/cambio")
#extrator = ExtratorUrl(None)
# valor_parametro = extrator.busca_parametro("moedaDestino")
print(extrator == extrator2)
