from math import pow
# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
# com a tabela abaixo:
# - Abaixo de 18,5: Abaixo do peso.
# - Entre 18,5 e 25: Peso ideal.
# - 25 até 30: Sobrepeso.
# - 30 até 40: Obesidade.
# - Acima de 40: Obesidade Mórbida.
# imc -> peso / altura(2)
peso = float(input('Digite seu peso em Kilos:'))
altura = float(input('Digite sua altura em metros:'))

imc = peso / pow(altura, 2)
if imc <= 18.5:
    print(f'Seu imc é {imc:.1f}. Você está abaixo do peso')
elif imc <= 25:
    print(f'Seu imc é {imc:.1f}. Você está no peso ideal')
elif imc <= 30:
    print(f'Seu imc é {imc:.1f}. Você está com sobrepeso')
elif imc <= 40:
    print(f'Seu imc é {imc:.1f}. Você está Obeso')
else:
    print(f'Seu imc é {imc:.1f}. Você está Morbidamente Obeso')
