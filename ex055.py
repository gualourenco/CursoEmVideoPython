# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lido.

lista = []

while len(lista) < 5:
    c = int(input('Insira um peso na lista: '))
    lista.append(c)

print(f'O maior peso da lista foi {max(lista)} e o menor foi {min(lista)}')

