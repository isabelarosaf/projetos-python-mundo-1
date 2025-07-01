frase = input('Digite seu nome completo: ').strip()

print('Seu nome em maiusculo: {}'.format(frase.upper()))

print('Seu nome em minusculo: {}'.format(frase.lower()))

print('Seu nome tem ao todo {} letras'.format(len(frase) - frase.count(' ')))

lista = frase.split()

print('O Total de letras em seu primeiro nome é: {}'.format(len(lista[0])))

