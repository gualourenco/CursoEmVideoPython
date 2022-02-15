# Desenvolva um programa que leia o primeiro termo ea razão de uma PA.
# No final, mostre os 10 primeiros termos dessa prograssão.
pt = int(input('Digite o primeiro termo para a progressão:\n'))
ra = int(input('Qual a razão aritmética:\n'))
resultado = pt + ra
lista = [resultado]
for c in range(1, 10):
    resultado = resultado + ra
    lista.append(resultado)
print(f'A Progreção Aritmética da razão de {ra} a partir do termo {pt} é {lista}')
