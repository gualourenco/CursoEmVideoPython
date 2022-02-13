# Faça um programa que leia uma frase pelo teclado e mostre:

frase = input('Escreva uma frase: ').strip().upper()

# Quantas vezes aparece a letra "A".
print('Quantas letras A? ')
print(frase.count('A'))

# Em que posição ela aparece a primeira vez.
print('Qual a posição do primeiro A?\n {}'.format(frase.find('A')+1))

# Em que posição ela aparece a última vez.
print('E a ultima posição do A?\n {}'.format(frase.rfind('A')+1))
