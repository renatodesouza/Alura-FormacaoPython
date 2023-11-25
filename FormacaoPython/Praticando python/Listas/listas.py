#O que são fatias (slices) em Python e como você as utiliza em uma lista?


lst = [x for x in range(0, 20)]

print(lst)

print(lst[:2])

print(lst[2:7])

print(lst[2:-2])

print(lst[-0:2])

for i in range(len(lst)):
    print(lst[i:i+4])