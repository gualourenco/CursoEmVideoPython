# Faça um programa que calcula a soma entre todos os números ímpares que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.
soma = 0
contagem = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contagem += 1
        soma += c
        print(c, end=' ')

print(f'\nA soma de todos os {contagem} números ímpares multiplos de 3, de 1 a 500 é {soma}')
