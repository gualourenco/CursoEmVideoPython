# Melhore o jogo do Desafio 028 onde o computador vai pensar em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpeites foram necessários,
# para vencer.

from random import randint, randrange
from time import sleep

numero = randrange(1, 11)
# randint(0, 10)
palpites = []
verif = 0

while verif == 0:
    num = int(input('Escolha um número de 0 a 10: '))
    print('Conferindo os números....')
    sleep(3)
    if num != numero:
        print(f'Errou!!!')
        verif = 0
        palpites.append(num)
        if num > 10:
            print('Favor digitar um número de 1 à 10')

    else:
        print(f'O número era {numero}.Você Venceu!')
        verif = 1

print(f'Você tentou {len(palpites) + 1} e chutou {palpites}')
