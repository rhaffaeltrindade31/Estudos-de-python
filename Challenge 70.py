print('=-='*10)
print('Loja super Baratão')
print('=-='*10)

while True:
    nomep = str(input('Qual o nome do produto? '))
    preco = int(input('Qual o preço do produto? '))

    while True:
        saida = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if saida in ('S', 'N'):
            break
        else:
            print('Digite somente S para (SIM) ou N para (NÃO)')

    if saida == 'N':
        break



