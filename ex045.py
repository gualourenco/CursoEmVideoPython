import random
# Crie um programa que faça o computador jogar Jokenpô com você.

pjogador = 0
pcomp = 0

jokenpo = ['Pedra', 'Papel', 'Tesoura']
mao_com = random.choice(jokenpo)
jogador = int(input('''Escolha:\n 1)Pedra\n 2)Papel\n 3)Tesoura\n'''))-1
mao_jogador = jokenpo[jogador]

if mao_com == jokenpo[0] and mao_jogador == jokenpo[1]:
    print('Papel engole Pedra. Você venceu')
elif mao_com == jokenpo[1] and mao_jogador == jokenpo[2]:
    print('Tesoura corta papel. Você venceu')
elif mao_com == jokenpo[2] and mao_jogador == jokenpo[0]:
    print('Pedra quebra tesoura. Voce venceu')
elif mao_com == jokenpo[1] and mao_jogador == jokenpo[0]:
    print('Papel engole Pedra. Você perdeu')
elif mao_com == jokenpo[2] and mao_jogador == jokenpo[1]:
    print('Tesoura corta papel. Você perdeu')
elif mao_com == jokenpo[0] and mao_jogador == jokenpo[2]:
    print('Pedra quebra tesoura. Voce perdeu')
elif mao_com == mao_jogador:
    print('Empatou. Jogue de novo')
else:
    print('Opção errada. Jogue de novo')
