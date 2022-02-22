# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# Desconsiderando o flag.

num = int(input('Digite um numero. 999 encerra a contagem:\n '))
lista = []
soma = 0
while num != 999:
    lista.append(num)
    soma += num
    num = int(input('Digite um número. 999 encerra a contagem:\n '))
print(f'os números digitados foram{lista}\nUm total de {len(lista)} números, e a soma deles é {soma}')
