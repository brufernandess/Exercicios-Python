# Exercícío 07 - Categoria por Idade na Natação
from datetime import date

print('-'*50)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO'.center(50))
print('-'*50)
print('Para descobrir sua categoria, digite abaixo o seu ano de nascimento')
nasc=int(input('\33[1;7mDATA:\33[m '))

ano= date.today().year
idade= ano - nasc

if idade <= 9:
    print(f'Você tem {idade} anos, sua categoria é: \33[4mMIRIM\33[m')
elif idade <=14:
    print(f'Voce tem {idade} anos, sua categoria é: \33[4mINFANTIL\33[m')
elif idade <=19:
    print(f'Voce tem {idade} anos, sua categoria é: \33[4mJUNIOR\33[m')
elif idade <=25:
    print(f'voce tem {idade} anos, sua categoria é: \33[4mSENIOR\33[m')
else:
    print(f'Voce tem {idade} anos, sua categoria é: \33[4mMASTER\33[m')

