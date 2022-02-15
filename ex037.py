# Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a Base de Conversão:
# -1 para Binário
# -2 para Octal
# -3 para Hexadecimal

numero = int(input('Digite um número inteiro para conversão de base: '))
option = int(input('Digite uma das opções de conversão abaixo:\n1- Binário\n2- Octal\n3- Hexadecimal\n'))

if option == 1:
    print('O numero {} em binário é {}'.format(numero, format(numero, 'b')))
elif option == 2:
    print('O numero {} em Octal é {}'.format(numero, format(numero, 'o')))
elif option == 3:
    print('O numero {} em Hexadecimal é {}'.format(numero, format(numero, 'X')))
else:
    print('Opção invalida. Tente novamente')

# ou

if option == 1:
    print('O numero {} em binário é {}'.format(numero, bin(numero)[2:]))
elif option == 2:
    print('O numero {} em Octal é {}'.format(numero, oct(numero)[2:]))
elif option == 3:
    print('O numero {} em Hexadecimal é {}'.format(numero, hex(numero)[2:].upper()))
else:
    print('Opção invalida. Tente novamente')
