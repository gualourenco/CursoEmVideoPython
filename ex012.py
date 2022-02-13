# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input('Qual o preço: '))
novopreco = n - (n * 0.05) # (n* 5 /100)

print(f'O valor saiu de R${n} para R${novopreco:.2f}')

