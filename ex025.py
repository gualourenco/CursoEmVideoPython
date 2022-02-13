# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome

nome = input('Escreva um nome: ').strip()
nome = nome.title()
print(f'O nome é {nome}')
print('tem Silva no nome?')
print('Silva' in nome)
