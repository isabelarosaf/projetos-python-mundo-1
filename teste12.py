numero = input("ME PASSA UM NUMERO ")

numero_inverso = numero[::-1]

contador = 0

for digito in numero_inverso:
    print(digito)
    if contador == 0:
        print('Unidade')
    elif contador == 1:
        print("Dezena")
    elif contador == 2:
        print("Centena")
    else:
        print("Milhar")

    contador += 1

    # feito pelo raphael /\


    # num = int(input('Informe seu nome: '))
    # u = num // 1 % 10
    # d = num // 10 % 10 
    # c = num // 100 % 10 
    # m = num // 1000 % 10 
    # print('Unidade: {}'.format(u))
    # print('Dezena: '.{}format(d))
    # print('Centena: '.{}format(c))
    # print('Milhar: '.{}format(m))
    