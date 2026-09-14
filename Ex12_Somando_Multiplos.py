# Exercício 12 - Somando múltiplos de 3 

print('-'*50)
print('SOMA MULTIPLOS DE 3 ENTRE 1 E 500'.center(50))
print('-'*50)
soma= 0
cont= 0
for c in range (1,501,2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')

