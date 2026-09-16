# Exercício 21 - Jogo de Adivinhar Utilizando While

from random import randint
from time import sleep

jogador = 0
palpites = 0

print('Vou pensar em um numero de 0 a 10...')
sleep(1)
computador = randint(0, 10)
acertou = False
while computador != jogador:
     jogador=int(input('Adivinha qual numero eu pensei: '))
     palpites +=1
     sleep(1)
     if computador == jogador:
         acertou = True
     else:
         if computador  < jogador:
             print('Menos... Tente novamente')
         elif computador > jogador:
             print('Mais... Tente novamente')

print('PARABÉNS, VOCÊ CONSEGUIU! 🎆')
print(f'Até voce acertar, voce teve {palpites} palpites')

