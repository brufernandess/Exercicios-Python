# Exercício 34 - Catálogo de Preços Utilizando Tuplas
listagem=('Maria Sasha 5d', 44, 'Decemars 5d', 44,'Fadvan Y', 24,'Escovinhas', 10, 'Microbrush', 10,'Pinça Nagaraku', 55)
print('='*50)
print('CATÁLOGO DE PREÇOS'.center(50))
print('='*50)


for pos in range (0,len(listagem)):
    if pos % 2 ==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('=' * 50)