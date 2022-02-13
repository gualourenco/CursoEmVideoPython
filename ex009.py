# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Qual o número: '))
m = 1
print('-'*20)
while m <= 10:
    print(f'{n} x {m} = {n*m}')
    m += 1
print('-'*20)
