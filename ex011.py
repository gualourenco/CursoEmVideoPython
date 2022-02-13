# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta,
# pinta uma área de 2m².

largura = float(input('Qual a largura: '))
altura = float(input('Qual a altura: '))
area = largura * altura
tinta = area / 2

print(f'Largura: {largura}m\nAltura: {altura}m\nArea: {area}m²\nSão {tinta}l de tinta')
