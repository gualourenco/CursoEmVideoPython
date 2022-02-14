# Desenvolva um programa que pergunte a distância de uma viagem em Km.
numero = int(input('Quantos kilometros de distancia tem a sua viagem? '))
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km
# E R$ 0,45 para viagens mais longas

# if numero <= 200:
#     print(f'Sua viagem será de {numero}Km, sua passagem será R$ {numero *0.50:.2f}')
# else:
#     print(f'Sua viagem será de {numero}Km, sua passagem será R$ {numero * 0.45:.2f}')

# ou
preco = numero * 0.50 if numero <= 200 else numero * 0.45
print(f'Sua viagem será de {numero}Km, sua passagem será R$ {preco:.2f}')
