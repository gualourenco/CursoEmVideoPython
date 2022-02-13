# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

n = float(input('Qual o salario: '))
novosal = n + (n * 0.15)

print(f'O valor saiu de R${n} para R${novosal:.2f}')
