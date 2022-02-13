# Crie um programa que leia o nome completo de uma pessoa e mostre:

nome = str(input('Digite um nome completo: ')).strip()
print(f'O nome escolhido foi: {nome.title()}')
# O nome com todas as letras maiusculas

print(f'Seu nome em maiuscula: {nome.upper()}')

# O nome com todas as letras minusculas

print(f'Seu nome em minuscula: {nome.lower()}')

# quantas letras ao todo (sem considerar espaços)

print('O nome sem espaços tem {} Caracteres '.format(len(nome) - nome.count(' ')))

# ou
print('Ou')
lista_nome = nome.split()
nova_lista_nome = ''.join(lista_nome)

print(f'O tamando de {len(nova_lista_nome)} caracteres, desse jeito')

# quantas letras tem o primeiro nome


print('Posso encontrar os {} caracteres com nome.find(): '.format(nome.find(' ')))
print('Ou')
print(lista_nome[0])
print(f'Com a nova lista, contando {len(lista_nome[0])} caracteres no primeiro item')
