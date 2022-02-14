# Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem
# ou não formar um triangulo.
# ex: a soma de das retas 1 e 2 maior que a reta 3
reta1 = float(input('Primeiro reta:'))
reta2 = float(input('Segunda reta:'))
reta3 = float(input('terceira reta:'))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('As retas formam um triângulo')
else:
    print('As retas não formam um triângulo')
