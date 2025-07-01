dias = float(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
valord = 60
valorkm = 0.15
v = (dias * valord) + (km * valorkm)
print('O preço a se pagar será {:.2f}.'.format( v ))