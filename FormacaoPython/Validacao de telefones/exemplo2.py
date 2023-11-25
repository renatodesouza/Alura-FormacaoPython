import re

padrao = "\w{1,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "atencao lucas213!teste.com.brazil renato123@gmail.com.br 345678ui lucas123@yahoo.com.br"

#Retorna somente a primeira corresposndencia encontrada no padrao
resposta = re.search(padrao, texto)


#Utilizando o findall que retorna uma lista com todas as correspondecias do padrao encontradas
resposta2 = re.findall(padrao, texto)

print(len(texto))
print(resposta.group())

print(resposta2)