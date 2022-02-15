# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

valor = 0
par = 0
for c in range(1, 7):
    numero = int(input(f'Digite 0 {c}° número inteiro: '))
    if numero % 2 == 0:
        valor += numero
        par += 1

print(f'Você digitou {par} pares, e a soma deles dá {valor}')
