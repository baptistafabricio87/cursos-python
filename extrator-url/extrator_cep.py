endereco = "Rua Renata Agondi 86, apto 55, Saboo, Santos, SP, 11085070"

import re # Regular Expression RegEx

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')

busca = padrao.search(endereco)
if busca:
   cep = busca.group()
   print(cep)
