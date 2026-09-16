# Exercício 22 - Menu de Opções

escolha= 1

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

while escolha !=5:
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos Numeros\n'
          '[5] Sair do Programa')

    escolha = int(input('Escolha o que deseja fazer com os numeros escolhidos: '))

    if escolha == 1:
        print(f'Você escolheu a opção 1. O resultado da soma entre os numeros {n1} e {n2} fica {n1+n2}.')
    elif escolha == 2:
        print(f'Você escolheu a opção 2. O resultado da multiplicação entre os numeros {n1} e {n2} fica {n1*n2}.')
    elif escolha ==3:
        if n1 > n2:
            print(f'Você escolheu a opção 3. O maior número entre {n1} e {n2} é {n1}')
        elif n1 == n2:
            print(f'Você escolheu a opção 3. O número {n1} e {n2} são iguais.')
        else:
            print(f'Você escolheu a opção 3. O maior número entre {n1} e {n2} é {n2}')
    elif escolha == 4:
        print('Informe os numeros novamente...')
        n1=int(input('Primeiro numero: '))
        n2=int(input('Segundo numero: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente Novamente!')


print('FIM DE PROGRAMA')