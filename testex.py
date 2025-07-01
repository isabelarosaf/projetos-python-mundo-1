# o nome com todas as letras maiusculas 
# o nome com todas as letras minusculas 
# quantas letras ao todo(sem considerar espaços)
# quantas as letras tem o primeiro nome 

n = input('Digite seu nome completo:')

maiusculas = n.upper()
print(maiusculas)

minuscula = n.lower()
print(minuscula)

splited = n.split(" ")
print("Variavel split:", splited)

juntar = "".join(splited)
print('Variavel juntar', juntar)

contar_letras = len(juntar)

print('Numero de letras', contar_letras)

print('Pegar palavra dentro do split', splited[0])

print('contando letras dentro de isa', len(splited[0]))


# nome = str(input('Digite seu nome completo:)).strip()  -o strip ta aqui para eliminar os espaços desnecess
# print('Seu nome em maiusculo é {}'.format(nome.upper()))
# print('Seu nome em letra minuscula é {}'.format(nome.lower()))
# print('Seu nome tem ao todo {} letras'.format(len.(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# ou 
# separar = nome.split()
# print('Seu primeiro nome é {} e ele tem {} letras'.format(separar[0], len(separar[0])))
