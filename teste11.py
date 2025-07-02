import random 
n = str(input('Digite um nome: '))
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
lista =  [n, n1, n2]
random.shuffle(lista)
print('A ordem aleatória decidida foi essa: {}.'.format (lista))