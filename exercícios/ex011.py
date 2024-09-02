lp = float(input('Largura da parede: '))
ap = float(input('Altura da parede: '))
area = lp*ap
litros = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lp, ap, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(litros))
