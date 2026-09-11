# Exercício 03 - Binário, Octal e Hexadecimal
numero=int(input('Digite um numero: '))



n1=int(input('Digite 1 para BINARIO, Digite 2 para OCTAL e 3 para HEXADECIMAL: '))



if n1 == 1:
    print(f'Voce escolheu a opção BINARIO, seu numero fica: {bin(numero)[2:]}')
elif n1 == 2:
    print(f'Voce escolheu a opção OCTAL, seu numero fica: {oct(numero)[2:]}')
elif n1 == 3:
    print(f'Voce escolheu a opção HEXADECIMAL, seu numero fica: {hex(numero)[2:]}')
else:
        print('OPÇÃO INVÁLIDA')