# Faça um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep

boom = ('!!! ' * 3)

for c in range(10, 5, -1):
    print(c)
    sleep(1)

for c in range(5, 0, -1):
    print(c)
    sleep(2)

print('.'*20)
sleep(3)
print('BOOOOOOOOMMMMMM!!!!!!!!')
