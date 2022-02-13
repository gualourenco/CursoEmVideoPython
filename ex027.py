# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

nome = str(input('Escreva um nome completo: ')).title().strip()
lista_nome = nome.split()
print('Primeiro nome: {}'.format(lista_nome[0]))
print('Seu ultimo nome é: {}'.format(lista_nome[len(lista_nome)-1]))
print('Seu ultimo nome é: {}'.format(lista_nome[-1]))
print('ou')
lista_nome_pop = lista_nome
print('Ultimo nome: {}'.format(lista_nome_pop.pop()))
lista_nome_pop = lista_nome
