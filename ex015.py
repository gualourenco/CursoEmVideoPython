# Escreva um programa que pergunte a quantidade de km percorrido
# por um carro alugado e a quantidade de dias pelos quais foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 p/ dia e R$ 0.15 por km rodado

km = float(input('informe km rodado: '))
dias = int(input('Informe quantos dias: '))

val_dias = 60 * dias
val_km = 0.15 * km

print(f'O carro andou um total de {km}km em {dias} dias. O valor total do aluguel ficou R$: {val_dias + val_km}')
