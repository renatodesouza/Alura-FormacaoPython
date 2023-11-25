import re

#Dado o seguinte padrao uma string que comece com 
#um numero de 0 a 9 o segundo item uma letra de a-z e o terceiro item um numero de 0 a 9

padrao = "[0-9][a-z][0-9]"

texto = "1b4 1a2 105"

#---------------------------------------------------
#Padrao dois uma string que comece com um numero de 0 a 9
#segundo e terceiro item uma letra de a-z
padrao2 = "[0-9][a-z][a-z]"

texto2 = "1c2 5b3 1du"

resposta = re.search(padrao, texto)

reposta2 = re.search(padrao2, texto2)

print(reposta2)

print(resposta.group())


