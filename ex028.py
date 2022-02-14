# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
from random import randint, randrange
from time import sleep
numero = randrange(1, 6)
randint(0, 5)
# o usuario tentar descobrir qual foi o número escolhido pelo computador.
num = int(input('Escolha um número de 0 a 5: '))
print('E o número foi....')
sleep(3)
# O programa deverá escrever na tela se o usuario venceu ou perdeu
if num == numero:
    print(f'O número era {numero}.Você Venceu!')
else:
    print(f'O número era {numero}.Você Perdeu')
