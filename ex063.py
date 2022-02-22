# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
num = int(input('Digite o número de repeticoes para a sequencia de fibonacci: '))

novovalor = 1
verif = 0
antigovalor = 0
total = 1

print(f'{total -1}', end='->')
while verif < num - 1:
    print(f'{total}', end='->')
    total = antigovalor + novovalor
    antigovalor = novovalor
    novovalor = total
    verif += 1
print('fim', end='')
