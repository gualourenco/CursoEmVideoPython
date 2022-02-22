# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valor entre os lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.
num = int(input('Digite um número: '))
verif = 'S'
lista = []
soma = 0
media = 0

while verif != 'N':

    lista.append(num)
    soma += num
    media = soma / len(lista)
    verif = str(input('Deseja continuar: [S] ou [N]')).upper()
    if verif == 'S':
        num = int(input('Digite um número: '))

print(f'A média entre os númmeros é {media}, sendo {max(lista)} o maior e {min(lista)} o menor')
