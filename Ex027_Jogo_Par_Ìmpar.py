# Exercício 27 - Jogo de Par ou Ímpar

from random import randint
from time import sleep

num=opcao=soma=resultado=0

print('-'*50)
print('JOGUINHO DO PAR OU ÍMPAR'.center(50))
print('-'*50)
sleep(1)
while True:
    num=int(input('Digite um número: '))
    opcao=str(input('Você acha que vai dar Par ou Ímpar?[P/I]: ')).upper()
    computador = randint (0,10)
    soma = computador + num


    print('-'*50)
    if soma % 2 ==0:
        resultado = 'P'
        print(f'Você jogou {num} e o computador {computador}. Total deu {soma:.0f} que é PAR ')
    else:
        resultado = 'I'
        print(f'Você jogou {num} e o computador {computador}. Total deu {soma:.0f} que é ÍMPAR')
    if opcao == resultado:
        print('Parabéns, você venceu! Vamos novamente...')
    else:
        break
print('VOCê PERDEU! GAME OVER')




