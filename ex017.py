# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retangulo, calcule e mostre o comprimento da hipotenusa.
from math import pow

cat_op = float(input('Qual o cateto oposto:'))
cat_ad = float(input('Qual o cateto adjacente:'))

hip = pow(cat_op, 2) + pow(cat_ad, 2)

print(f'{cat_op}² + {cat_ad}² = {hip}')
