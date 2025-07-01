frase = str(input('Escreva uma frase: ')).strip()
frase = frase.upper()
frase = frase.replace('Á','A')
frase = frase.replace('À','A')
frase = frase.replace('Â','A')
frase = frase.replace('Ã','A')


contar_a = frase.count('A')

print('A letra A aparecer {}.'.format(contar_a))

encontrar_primeiravez = frase.find('A')

print('A letra A aparece pela primeira vez em {} lugar.'.format(encontrar_primeiravez))

encontrar_ultimapalavra = frase.rfind('A')

print('A Ultima vez que a letra A aparece é em {} lugar.'.format(encontrar_ultimapalavra))