# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

numero = int(input('Digite o número desejado para ver a tabuada:\n'))

for c in range(1, 11):
    print(f'{numero} x {c} = {numero * c:.0f}')
