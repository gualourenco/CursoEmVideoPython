# escreva um programa que converterá uma temperatura digitando em graus Celsius,
# e converta para Fahrenheit.

c = float(input(('Quantos Graus: ')))
f = ((c * 9) / 5) + 32

print(f'{c}°C Celsius viram {f}°F em Fahrenheit')
