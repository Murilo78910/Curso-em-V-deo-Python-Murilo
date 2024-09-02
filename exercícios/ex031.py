distancia = float(input('Qual é a distância da viajem? '))
print('Você está prestes a começar uma viajem de {:.1f}Km.'.format(distancia))
v1 = distancia * 0.50
v2 = distancia * 0.45
if distancia < 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(v1))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(v2))
