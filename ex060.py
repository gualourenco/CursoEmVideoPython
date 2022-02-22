# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120.

num = float(input('Digite um valor para começarmos o Fatorial: '))
print(f'{num:.0f}! = ', end='')
verif = num
fatorial = 1
listaf = []
while verif > 0:
    fatorial *= verif
    listaf.append(fatorial)
    verif -= 1
print(f'{num:.0f}', end='')
c = num
while c != 1:
    print(f' x {c - 1:.0f}', end='')
    c -= 1
print(f' = {fatorial:.0f}')
