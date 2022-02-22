# Refaça o desafio 051, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.
pt = int(input('Digite o primeiro termo para a progressão:\n'))
ra = int(input('Qual a razão aritmética:\n'))
decimo = pt + (10 - 1) * ra
verif = 10
soma = pt

while verif > 0:
    print(f'{soma} ', end='-> ')
    soma += ra
    verif -= 1
print('fim')
