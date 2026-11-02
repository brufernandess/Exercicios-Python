# Exercício 37 - Cálculos Utilizando Listas

num= []
media=soma=0
for c in range (1,8):
    num.append(int(input('Digite um número: ')))

maior = max (num)
menor = min (num)
media = sum(num) / len(num)
print(f'O maior número é {maior} e o menor número é {menor}')
print(f'Encontrei o número {maior} nas posições ',end='')
for p, v in enumerate (num):
    if v == maior:
        print(f'{p+1}...',end='')
print(f'\nEncontrei o número {menor} nas posições ',end='')
for p, v in enumerate (num):
    if v == menor:
        print(f'{p+1}...',end='')
print(f'\nA média dos números digitados foram: {media:.1f}')
