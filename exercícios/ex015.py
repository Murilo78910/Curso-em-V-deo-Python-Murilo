di = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
dr = di * 60
kmr = km * 0.15
valor = dr + kmr
print('O total a pagar é de R${}'.format(valor))
