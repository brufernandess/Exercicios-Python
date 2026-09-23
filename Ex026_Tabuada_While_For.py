# Exercício 26 - Tabuada Utilizando While e For (Digite número negativo para parar)

num = 0

while num >= 0:
    num=int(input('Digite um número que gostaria de saber a tabuada: '))
    if num < 0:
        break
    print('-'*50)
    print(f'TABUADA DO {num}'.center(50))
    print('-'*50)

    for i in range (1,11):
        print(f'{i} x {num} = {i * num} ')
        i += 1

print('-------NÚMERO INVÁLIDO. PROGRAMA ENCERRADO------')
