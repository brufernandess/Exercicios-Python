# Exercício 13- Calculando a Tabuada 

from time import sleep
print('-'*50)
print('CALCULE A TABUADA'.center(50))
print('-'*50)

num=int(input('Digite um numero que gostaria de saber a tabuada: '))
sleep (1)
print('AGUARDE...')
print('-'*50)
sleep (1)

for c in range (1,11):
    print(f'{c:2} X {num} = {c*num}')

print('FIM DA TABUADA')