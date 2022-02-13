# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dolares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27

bolso = float(input('Quanto você gostaria de converter: '))
dol = 3.27
print(f'R${bolso} podem comprar US${bolso / dol:.2f} ')
