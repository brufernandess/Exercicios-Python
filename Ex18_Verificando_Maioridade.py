# Exercício 18 - Verificando Maioridade


maior= 0
menor= 0
for pessoas in range (1,8):
    data=int(input(f'Em que ano a {pessoas}º pessoa nasceu?: '))
    idade = 2026 - data

    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'Existe {maior} pessoas maior de idade')
print(f'Existe {menor} pessoas menor de idade')
