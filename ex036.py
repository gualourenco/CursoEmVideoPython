# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o Valor da casa, o Salário do comprador e em Quantos anos ele vai pagar.
# Calcule o valor da prestação mensal.
# Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

imovel = float(input('Digite o valor do imovel: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite a quatidade e anos para o financiamento:'))

parcela = imovel / (anos * 12)
print(f' A parcela está em R$ {parcela:.2f}')

if parcela <= (salario * 0.30):
    print('Crédito aprovado!')
else:
    print('Crédito negado. Volte duas casas')
