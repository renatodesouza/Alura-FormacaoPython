import requests
from acesso_cep import CEP

cep = '08441260'

obj_cep = CEP(cep)

rua, bairro, localidade, uf = obj_cep.acessa_via_cep()


print(rua, bairro, localidade, uf)