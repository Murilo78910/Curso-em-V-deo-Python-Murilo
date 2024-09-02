'''nome = (str(input('Qual é o seu nome? ')))
if nome == 'Murilo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal.')
#print(f'Bom dia, {nome}')
print('Bom dia, {}'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
