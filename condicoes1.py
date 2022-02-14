# Exemplos de condição

# tempo = int(input("quantos anos tem seu carro? "))
# if tempo <= 3:
#     print('Carro novo')
# else:
#     print('Carro velho')
# print('--FIM--')
#
# print('Carro novo' if tempo <= 3 else 'Carro velho')
# print('--FIM--')
#
# nome = str(input('Qual o seu nome? ')).title()
# if nome == 'Gustavo':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é um nome')
# print(f'Bom dia {nome}')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua media foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! PARABENS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
