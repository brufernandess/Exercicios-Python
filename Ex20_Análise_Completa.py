# Exercício 20 - Analisando Informações 

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulheres= 0

from time import sleep
for p in range (1,5):
    print(f'----{p}º Pessoa----')
    nome=str(input('Digite seu nome: ')).strip()
    idade=int(input('Digite sua idade: '))
    sexo=str(input('Digite o seu sexo [F/M]: ')).strip()
    sleep (1)
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1




media_idade= soma_idade / 4
print(f'A média de idade das pessoas é de {media_idade:.0f} anos')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {nome_velho}')
print(f'Existem {mulheres} abaixo de 20 anos')