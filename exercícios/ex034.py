'''sl = float(input('Qual é o salário do funcionário? R$'))
dez = sl + (sl * 10/100)
qui = sl + (sl * 15/100)
if sl <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sl, qui))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sl, dez))'''

sl = float(input('Qual é o salário do funcionário? R$'))
if sl <= 1250:
    novo = sl + (sl * 15 / 100)
else:
    novo = sl + (sl * 10 / 100)
    
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sl, novo))
