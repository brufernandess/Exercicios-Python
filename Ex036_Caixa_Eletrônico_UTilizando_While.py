# Exercício 36 - Caixa Eletrônico Utilizando While
print('###'*10)
print('CAIXA ELETRONICO'.center(30))
print('###'*10)

valor=int(input('Digite o valor que gostaria de sacar: R$'))
while True:
    if valor >= 100:
        cont100= valor // 100
        valor = valor - cont100 * 100
        print(f'Cédulas de R$100 reais: {cont100}')
        if not valor:
            break
    if valor >= 50:
        cont50 = valor // 50
        valor = valor - cont50 * 50
        print(f'Cédulas de R$50 reais: {cont50}')
        if not valor:
            break
    if valor >= 20:
        cont20 = valor // 20
        valor = valor - cont20 * 20
        print(f'Cédulas de R$20 reais: {cont20}')
        if not valor:
            break
    if valor >=10:
        cont10= valor // 10
        valor = valor - cont10 * 10
        print(f'Cédulas de R$10 reais: {cont10}')
        if not valor:
            break
    if valor >= 5:
        cont5 = valor // 5
        valor= valor - cont5 * 5
        print(f'Cédulas de R$5 reais: {cont5}')
        if not valor:
            break
    if valor:
        cont1 = valor // 1
        valor = valor - cont1 * 1
        print(f'Cédulas de R$1 real: {cont1}')
        break

