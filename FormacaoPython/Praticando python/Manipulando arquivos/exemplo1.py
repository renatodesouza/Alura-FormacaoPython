
import os

#Criando um arquivo e escrevendo dentro dele
with open('arquivo.txt', 'w') as arq:

    arq.write('conteudo do arquivo, ')


with open('arquivo.txt', 'a') as arq:
    arq.write('\nAdicionando mais conteudo a um arquivo existente')


#Lendo um conteudo do arquivo
with open('arquivo.txt', 'r') as arq:
    conteudo = arq.read()

print(conteudo)


if os.path.isfile('arquivo.txt'):
    print('Arquivo encontrado')
else:
    print('Arquivo não encontrado')