# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
pt = int(input('Digite o primeiro termo para a progressão, ou 0 para encerrar o programa:\n'))
ra = int(input('Qual a razão aritmética:\n'))
decimo = pt + (10 - 1) * ra
verif = 10
soma = pt
while pt != 0:

    while verif > 0:
        print(f'{soma} ', end='-> ')
        soma += ra
        verif -= 1
    print('fim')
    pt = int(input('Digite o primeiro termo para a progressão, ou 0 para encerrar o programa:\n'))
    ra = int(input('Qual a razão aritmética:\n'))
    decimo = pt + (10 - 1) * ra
    verif = 10
    soma = pt
