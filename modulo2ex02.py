print('----'*20)
print('----------EMPRESTIMO BANCARIO----------')
print('----'*20)
casa=float(input('Digite o valor da casa: R$'))
salario=float(input('Digite seu salário: R$'))
anos=int(input('Digite em quantos anos voce deseja pagar: '))

pc= (casa/anos)/12
porcentagem= (salario*30 /100)

if pc >= porcentagem:
    print(f'Infelizmente seu emprestimo \33[4;7mNÃO\33[m foi aprovado')
else:
    print(f'\33[1;30;45mParabens! Seu emprestimo foi aprovado!\33[m')