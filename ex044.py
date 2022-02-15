# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu Preço normal e
# Condição de Pagamento:
# - À vista dinheiro/cheque: 10% de desconto.
# - À vista no cartão: 5% de desconto.
# - Em até 2x no cartão: Preço normal.
# - 3x ou mais no cartão: 20% de juros

valor = float(input('digite o valor total da compra: '))
vista = valor - (valor * 0.10)
debito = valor - (valor * 0.05)
parcela2 = valor
parcela3 = valor + (valor * 0.20)

print(f'''\nEscolha uma forma de pagamento:
1) À vista no dinheiro ou cheque: -10%
2) À vista no débito ou crédito: -5%
3) Em até 2x no crédito: Valor normal
4) Em 3x ou mais no crédito: 20% de acréscimo''')

opcao = int(input())

if opcao == 1:
    print(f'Sua compra no valor de R$ {valor}, ficará por R$ {vista}')

elif opcao == 2:
    print(f'Sua compra no valor de R$ {valor}, ficará por R$ {debito}')

elif opcao == 3:
    vezes = int(input('1 ou 2 parcelas?'))

    if vezes == 1:
        print(f'Sua compra no valor de R$ {valor}, ficará por R$ {parcela2//vezes}')

    else:
        print(f'Sua compra no valor de R$ {valor}, ficará por R$ {parcela2//vezes} por parcela')

elif opcao == 4:
    vezes = int(input('Quantas parcelas?'))
    print(f'Sua compra no valor de R$ {valor}, ficará por R$ {parcela3//vezes} por parcela,'
          f' no total de {parcela3}')

else:
    print('Opção errada. Refaça a sua compra.')
