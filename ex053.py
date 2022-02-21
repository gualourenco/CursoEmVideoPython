# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
# Ex: Apos a Sopa

frase = str(input('Digite uma frase no verificador de palindromo:\n')).strip().upper()
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

# ou

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso2 = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso2 == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
