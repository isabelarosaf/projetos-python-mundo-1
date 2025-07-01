nome = str(input('Digite seu nome: ')).strip()

nome = nome.upper()

nome_splitado = nome.split(' ')

print(nome_splitado)

encontrar_silva = 'SILVA' in nome_splitado

print(encontrar_silva)