# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número para sabermos se é primo:\n'))
if num % 2 == 0:
    if num == 2:
        print(f'O numero {num} é primo')
    else:
        print(f'O numero {num} não é primo')

elif num % 3 == 0:
    if num == 3:
        print(f'O numero {num} é primo')
    else:
        print(f'O numero {num} não é primo')
else:
    print(f'O numero {num} é primo')
