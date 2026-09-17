# Exercício 24 - Progressão Aritmética

primeiro=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))

count = 1
termo = primeiro
mais= 10
total= 0
while mais !=0:
    total = total + mais
    while count <= total:
        print(f'{termo} -->', end='')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais?: '))
print(f'Progressão finalizada com {total} termos mostrados')


