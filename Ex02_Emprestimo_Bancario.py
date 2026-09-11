# Exercício 02 - Simulando um emprestimo
print('-'*80)
print('EMPRESTIMO BANCARIO '.center(80))
print('-'*80)
casa=float(input('Digite o valor da casa: R$'))
salario=float(input('Digite seu salário: R$'))
anos=int(input('Digite em quantos anos voce deseja pagar: '))

pc= (casa/anos)/12
porcentagem= (salario*30 /100)
print(f'Para pagar uma casa de {casa}, sua prestação fica {pc:.2f} em {anos} anos')
if pc >= porcentagem:
    print(f'Infelizmente seu emprestimo \33[4;7mNÃO\33[m foi aprovado')
else:
    print(f'\33[1;30;45mParabens! Seu emprestimo foi aprovado!\33[m')