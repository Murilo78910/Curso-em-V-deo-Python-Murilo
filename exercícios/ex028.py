import random
import time

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = int(input('Em que número você pensou? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
time.sleep(3) # Serve para "dormir" por 3 segundos
al = random.randint(0,5) # Faz o computador "PENSAR"
if num == al:
    print('PARABÉNS! Você conseguiu me vencer! Eu pensei no {}'.format(al)) # Se o número que o jogador digitar for igual ao número que o computador pensou o jogador vence!!!
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(al, num)) # Se o jogador errar quem vence é o computador!!!
