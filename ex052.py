# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo, retornando de 0 até o mesmo.
num = int(input('Digite um número para sabermos se é primo:\n'))

for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')

if num % 2 == 0:
    if num == 2:
        print(f'\nO numero {num} é primo')
    else:
        print(f'\nO numero {num} não é primo')
elif num % 3 == 0:
    if num == 3:
        print(f'\nO numero {num} é primo')
    else:
        print(f'\nO numero {num} não é primo')
else:
    print(f'\nO numero {num} é primo')
