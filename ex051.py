# Desenvolva um programa que leia o primeiro termo ea razão de uma PA.
# No final, mostre os 10 primeiros termos dessa prograssão.
pt = int(input('Digite o primeiro termo para a progressão:\n'))
ra = int(input('Qual a razão aritmética:\n'))
decimo = pt + (10 - 1) * ra
for c in range(pt, decimo + ra, ra):
    print(f'{c} ', end='-> ')
print('fim')
