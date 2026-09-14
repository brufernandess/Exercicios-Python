# Exercício 17 - Verificando Palindromo

frase=str(input('Digite uma frase: ')).strip().upper()

palavras= frase.split()
junto= ''.join(palavras)
inverso= junto[:: -1]

print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('TEMOS UM PALINDROMO')
else:
    print('NÃO TEMOS UM PALÍNDROMO')
