lst = [12, 24, 11, 45]

lst_2 = [16, 77, 99, 54, 12]

#Crio uma copia da lst
nova_lst = lst.copy()

#Extendo a lista 2 com a nova lst e recebo valores duplicados
nova_lst.extend(lst_2)

print(nova_lst)

print(set(nova_lst))

lst = {12, 24, 11, 45}

lst_2 = {16, 77, 99, 54, 12}

#Pipe "|" sgnifica "ou" e funciona semelhante ao extend
print(lst | lst_2)

#Retorna somente os elementos que estao nas duas listas
print(lst & lst_2)

#retorna lst menos "nao retorna" lst_2
print(lst - lst_2)
