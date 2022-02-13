# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input('Qual o nome da cidade: ').strip()
cidade = cidade.title()
print(f'O nome da cidade foi {cidade}')
print('Cidade tem Santo no nome?')
print('Santo' in cidade)
print(cidade[:5] == 'Santo')
