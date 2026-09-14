# Exercício 14 - Calculando Números Pares

        
soma= 0
count= 0
for c in range (1,7):
    num=int(input('Digite um numero: '))

    if num % 2 == 0:
        soma += num
        count += 1
print(f'Você informou {count} numeros PARES, e a soma dos valores são: {soma}')