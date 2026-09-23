# Exercício 28 - Analisando Dados do Grupo



total=idade=cont=homens=mulheres=maior=0

while True:
    idade=int(input('Digite sua idade: '))
    sexo= ' '
    while sexo not in 'MF':
        sexo=input('Qual seu sexo? [F/M]: ').upper().strip()[0]

        total += 1
        cont += idade
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20 :
        mulheres += 1

    resp = ' '
    while resp not in 'SN':
        resp=str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print(f'São {homens} homens cadastrados, e {mulheres} mulheres abaixo de 20 anos\n'
      f'E são {maior} pessoas maiores de 18 anos')

