import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
print('O ângulo de {} tem o COSSENO {:.2f}'.format(an, cosseno))
print('O ângulo de {} ten a TANGENTE {:.2f}'.format(an, tangente))
