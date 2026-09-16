# Exercício 23 - Calculando Número Fatorial

n=int(input('Digite um numero que gostaria de calcular o fatorial: '))
c= n
f= 1
print(f'Calculando {n}!=')
while c > 0:
    print(f'{c}' ,end='')
    print('X ' if c > 1 else '=',end='')
    f *= c
    c -= 1
print(f'{f}')