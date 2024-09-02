ve = float(input('Qual é a velocidade atual do carro? '))
if ve > 80:
    print('MULTADO! Você exedeu o limite  permitido que é 80Km/h')
    multa = (ve - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Bom dia! Dirija com segurança.')
