# Exercício 16 - Verificando Números Primos

print('-'*50)
print('DESCUBRA SE O NUMERO É PRIMO OU NÃO'.center(50))
print('-'*50)

num=int(input('Digite um numero: '))
tot = 0
for c in range (1, num + 1 ):
    if num % c == 0:
        tot += 1
        print('\33[32m', end= '')
    else:
        print('\33[31m', end= '')
    print(f'{c}', end= '')
print(f'\n\33[mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('È por isso que ele é PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')

