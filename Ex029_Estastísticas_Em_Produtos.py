# Exercío 29 - Estastísticas em Produtos
print('--*--'*10)
print('LOJA SUPER TOP'.center(50))
print('--*--'*10)

resp='Ss'
produto=preco=total=maiscaro=menor=quant=maior=menorproduto=0
while resp in 'Ss':

    produto=(input('Nome do produto: '))
    preco=float(input('Preço: R$ '))
    resp=input('Quer continuar?[S/N]: ')

    total += preco
    quant +=1
    if quant == 1:
            menor = preco
            maior = preco
            menorproduto = produto
    else:
        if preco < menor:
            menor = preco
            menorproduto = produto
        if preco > maior:
              maior = preco
    if preco > 1000:
        maiscaro += 1
print(f'O valor total da compra deu R${total}\n'
      f'São {maiscaro} produtos acima de R$1.000 reais\n'
      f'O produto mais barato foi o {menorproduto.upper()} que custou R${menor} reais')
