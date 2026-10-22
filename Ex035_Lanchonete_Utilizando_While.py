# Exercício 35 - Lanchonete Utilizando While
print('='*50)
print('1- Coxinha - R$5,00\n'
      '2- Pastel  - R$7,00\n'
      '3- Café    - R$4,00\n'
      '4- Suco    - R$6,00\n'
      '5- Sair    ')
print('='*50)
total= 0

while True:
    produto=int(input('Selecione o item que gostaria de comprar: '))

    if produto == 1:
        qtd=int(input('Quantas unidades gostaria?: '))
        total = total + qtd * 5.00
    elif produto == 2:
        qtd=int(input('Quantas unidades gostaria?: '))
        total = total + qtd * 7.00
    elif produto == 3:
        qtd=int(input('Quantas unidades gostaria?: '))
        total = total + qtd * 4.00
    elif produto == 4:
        qtd=int(input('Quantas unidades gostaria?: '))
        total = total + qtd * 6.00
    elif produto == 5:
        break
    else:
        print('Produto Inválido. Tente novamente!')

print(f'O total da sua compra foi de R${total}')