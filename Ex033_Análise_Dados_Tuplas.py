# Exercício 33 - Análise de Dados em Tuplas

n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo número: '))
n3=int(input('Digite o terceiro número: '))
n4=int(input('Digite o quarto número: '))


numeros = (n1,n2,n3,n4)

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if 3 not in numeros:
    print('O número 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}º posição  ')
print('Os números pares são: ',end='')
for numero in numeros:
    if numero % 2==0:
        print(numero,end=' ')