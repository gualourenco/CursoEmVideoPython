# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
# Ex: Apos a Sopa

frase = str(input('Digite uma frase no verificador de palindromo:\n'))
nova = frase.replace(' ', '')
b = -1
cont = len(nova)

for c in range(0, len(nova)):
    if nova[c] == nova[b]:
        b -= 1
        cont -= 1
        if cont == 0:
            print(f'A frase {frase} é palindromo')
    else:
        print(f'A frase {frase}, não é palindromo')
