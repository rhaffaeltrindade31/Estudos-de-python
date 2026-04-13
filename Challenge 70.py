soma = totmil = menor = cont = 0 
barato = ''
print('=-='*10)
print('Loja super Baratão')
print('=-='*10)

while True:
    nomep = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto? '))
    soma += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nomep
   
    if preco > 1000:
        totmil += 1

    while True:
        saida = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if saida in ('S', 'N'):
            break
        else:
            print('Digite somente S para (SIM) ou N para (NÃO)')

    if saida == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi {soma}')
print(f'Teve {totmil} produto acima de 1000 reias')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')




