# Escreva um programa que leia Dois Números inteiro e compare-os, mostrando na tela uma mensagem:
# - O primeiro Valor é Maior.
# - O segundo valor é maior.
# - Não existe valor maior, os dois são iguais.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O primeiro numero é maior')
elif n1 < n2:
    print('O segundo numero é maior')
else:
    print('Não existe valor maior, os dois são iguais')
