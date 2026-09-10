# Exercicio 09 - Simulando Compras e Taxas
valor=float(input('Digite o valor do produto: R$ '))

opcao=int(input('[1] À vista dinheiro/cheque \n'
      '[2] À vista no cartão\n'
      '[3] Em 2x Cartão\n'
      '[4] 3x ou mais Cartão\n'
                'Escolha umma das opçoes de pagamento: '))
desavis= valor - (valor * 10 / 100)
descart= valor - (valor * 5 / 100)
juros= valor + (valor * 20 / 100)

if opcao == 1 :
    print(f'[1] Para pagamento a vista oferecemos 10% de desconto, seu produto ficou: R${desavis:.2f} ')
elif opcao == 2 :
    print(f'[2] Para pagamento a vista no cartão oferecemos 5% de desconto, seu produto ficou: R${descart:.2f}')
elif opcao == 3 :
    print(f'[3] Para pagamento em ate 2x oferecemos a opção de parcelamento sem juros, seu produto ficou: 2x R${valor/2} ')
elif opcao == 4 :
    print(f'[4] Para pagamento a partir de 3x, tem acrescimo de 20%, seu produto ficou: R${juros}')
else:
    print('Digite uma opção válida!')
    