sl = float(input('Qual é o salário do funcionário?R$:'))
au = sl + (sl * 15 / 100)
print('Um funcionário que ganhava R${:.3f}, com 15% de aumento, passa a receber R${:.3f}'.format (sl, au))
