cidade = str(input('Digite o nome de sua cidade: ')).strip()

cidade_capitalizada = cidade.capitalize()

cidade_em_partes = cidade_capitalizada.split(' ')

tem_santo = 'Santo' in cidade_em_partes[0]

# print(cidade[:5])

print(tem_santo)
