from time import sleep

nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
sleep(1)
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
nl = len(nome.strip().replace(' ', ''))
print('Seu nome tem ao todo {} letras'.format(nl))
pm = nome.split()
a = len(pm[0])
print('Seu primeiro nome tem {}'.format(a))