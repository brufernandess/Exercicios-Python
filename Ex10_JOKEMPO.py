# Exercicio 10 - JOKEMPO
import random

print('-'*50)
print('VAMOS BRINCAR UM POUQUINHO?'.center(50))
print('-'*50)

print('[1] PEDRA   🪨 \n'
      '[2] PAPEL   📄\n'
      '[3] TESOURA ✂️')
jogador=int(input('ESCOLHA UM ALTERNATIVA: '))


jogo= ['pedra','papel','tesoura']

computador = random.choice(jogo)


if jogador == 1 and computador == 'pedra':
    print('EMPATE! TENTE NOVAMENTE!🪨')
elif jogador == 2 and computador == 'papel':
    print('EMPATE, TENTE NOVAMENTE!📄')
elif jogador == 3 and computador == 'tesoura':
    print('EMPATE, TENTE NOVAMENTE!✂️')
elif jogador ==1 and computador =='papel':
    print(f'Poxa, voce perdeu! Eu escolhi PAPEL📄 e voce escolheu PEDRA🪨 ')
elif jogador ==2 and computador =='pedra':
    print(f'Parabens, voce ganhou! Voce escolheu  PAPEL📄 e eu escolhi PEDRA🪨 ')
elif jogador ==3 and computador =='pedra':
    print(f'Poxa, você perdeu! Eu escolhi PEDRA🪨 e você TESOURA✂️')
elif jogador ==1 and computador =='tesoura':
    print(f'Parabens, voce ganhou! Voce escolheu PEDRA🪨 e eu escolhi TESOURA✂️')
elif jogador ==2 and computador =='tesoura':
    print(f'Poxa, você perdeu! Eu escolhi TESOURA✂️ e você PAPEL📄')
elif jogador ==3 and computador =='papel':
    print(f'Parabéns, voce ganhou! Você escolheu TESOURA✂️ e eu escolhi PAPEL📄')
else:
    print('OPÇÃO INVÁLIDA!')
    