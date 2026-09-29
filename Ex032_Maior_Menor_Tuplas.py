# Exercício 32 - Verificando Maior e Menor utilizando TUPLAS
from random import randint
numeros= ()
numero=0
print('Os números sorteados foram: ',end='')
for i in range (5):
    numero = randint(1,10)
    numeros += (numero,)
    print(f'{numero}',end=' ')

print(f'\nO maior numero foi {max(numeros)} e o menor numero foi {min(numeros)}')


