import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hipo = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
