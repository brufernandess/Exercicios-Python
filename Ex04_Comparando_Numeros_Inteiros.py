n1=int(input('Digite um numero: '))
n2=int(input('Digite mais um numero: '))

if n1 > n2:
    print(f'O numero \33[4;7m{n1}\33[m é maior que o numero \33[4;7m{n2}\33[m')
elif n2 > n1:
    print(f'O numero \33[4;7m{n2}\33[m é maior que o numero \33[4;7m{n1}\33[m')
else:
    print('Não existe valor maior, os dois são iguais!')