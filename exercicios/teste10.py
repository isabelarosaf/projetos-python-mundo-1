import math
a = float(input('Digite o comprimento do cateto adjacente: '))
o = float(input('Digite o comprimento do cateto oposto: '))
q = a ** 2 + o ** 2
r = math.sqrt(q)
print('A hipotenusa vai medir {:.2f}'.format(r))


