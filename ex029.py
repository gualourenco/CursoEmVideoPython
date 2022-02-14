# Escreva um programa que leia a velocidade de um carro.
km = int(input('Digite a velocidade: '))
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite
# if km <= 80:
#     print('Você está dentro do limite de velocidade')
# else:
#     print('Você está acima do limite de 80Km')
#     print(f'Pague R$ {(km - 80) * 7.00:.2f} de multa pelo excesso')

if km > 80:
    print('Você está acima do limite de 80Km')
    print(f'Pague R$ {(km - 80) * 7.00:.2f} de multa pelo excesso')
print('Você está dentro do limite')
