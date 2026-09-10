# Exercicio 08 - Calculo De IMC
print('-'*50)
print('\33[7MCALCULO DE IMC\33[M'.center(50))
print('-'*50)

peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'ATENÇÂO, seu IMC está {imc:.2f}. Voce está ABAIXO do peso ideal.')
elif imc < 25:
    print(f'Parabens, seu IMC está {imc:.2f}. Voce está no seu peso IDEAL!')
elif imc < 30:
    print(f'ATENÇÃO, seu IMC está {imc:.2f}. Voce esta em SOBREPESO.')
elif imc < 40:
    print(f'ATENÇÃO, seu IMC está {imc:.2f}. Voce esta em OBESIDADE.')
else:
    print(f'Muita atenção, seu IMC está {imc:.2f}. Voce está em OBESIDADE MORBIDA')