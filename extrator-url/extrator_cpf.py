usuario = "Fabricio Castro, 19/04/1987, 333.888.444-11"
# usuario = "Fabricio Castro, 19/04/1987, 33388844411"

import re

padrao = re.compile('[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}')
busca = padrao.search(usuario)

if busca:
    cpf = busca.group()
    print(cpf)