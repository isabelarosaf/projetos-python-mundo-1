nome = str(input('Digite seu nome completo: ')).strip()

print('Muito prazer em te conhecer!')

tornar_lista = nome.split(' ')

print('Seu primeiro nome é: {}.'.format(tornar_lista[0]))

print('Seu último nome é: {}.'.format(tornar_lista[-1]))
