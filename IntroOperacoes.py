print('Estou aprendendo Python')

nome = 'Guanabara'
idade = 25
peso = 75.8
print(nome, idade, peso)

# nome = input('Qual seu nome?')
# idade = input('Qual sua idade?')
# peso = input('Qual seeu peso?')

# crie um script Pyton que leia o nome de uma pessoa
# e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

# nome = input('Qual seu nome?')
# print('Olá', nome, '! Seja bem vindo!')

# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa
# e mostre uma mensagem com a data formatada

# dia = input()
# mes = input()
# ano = input()
# print(dia, '/', mes, '/', ano)

# Crie um scrip Python que leia dois numeros e tente mostrar a soma entre eles

a = int(input("primeiro numero: "))
b = int(input('Segundo numero: '))
print('A Soma de', a, '+', b, 'é', a+b)

print('='*20)

nome = str(input('Qual o nome'))
print('Prazer em te conhecer {:>20}'.format(nome))
print('Prazer em te conhecer {:<20}'.format(nome))
print('Prazer em te conhecer {:^20}'.format(nome))
print(f'Prazer em te conhecer {nome:=^20}')

x = 5
y = 2

# + adicao
adic = x + y
print(adic)
# - subtracao
sub = x - y

# * multiplicacao
multi = x + y

# / divisao
div = x / y

# ** potenciacao
potenc = x ** y

# // divisao inteira
divint = x // y

# % resto da divisao
restodiv = x % y

# raiz quadrada 8**(1/2)

print(f'A soma é {adic}\nA sobra é {sub}\nE produto é {multi}\nE a divisao é {div:.3f}\n', end='>>>')
print(f'A Divisao inteira é {divint}\nA potencia é {potenc}', end='<<<')
