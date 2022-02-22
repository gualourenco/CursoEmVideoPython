# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar.
# [2] multiplicar.
# [3] maior.
# [4] novos números.
# [5] sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.

option = 0
verif = 0
num1 = int(input('Insira um primeiro valor: '))
num2 = int(input('Agora o segundo valor:'))
while verif == 0:
    print('------- Menu --------')
    print('''
     [1] somar.
     [2] multiplicar.
     [3] maior.
     [4] novos números.
     [5] sair do programa.
    ''')
    option = int(input('Qual a sua opção?'))
    if option == 1:
        print(f'A soma de {num1} e {num2} é {num1 + num2}')
        verif = 0
    elif option == 2:
        print(f'A multiplicação de {num1} e {num2} é {num1 * num2}')
        verif = 0
    elif option == 3:
        maior = [num1, num2]
        print(f'O número maior entre entre os escolhidos é {max(maior)}')
        verif = 0
    elif option == 4:
        num1 = int(input('Insira um primeiro valor: '))
        num2 = int(input('Agora o segundo valor:'))
        verif = 0
    elif option == 5:
        print('Encerrando o programa.\nAté mais!')
        verif = 1
    else:
        print('Favor, digitar uma das opções acima')
        verif = 0
