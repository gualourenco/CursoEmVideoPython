# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
salario = float(input('Digite o valor do salário: '))
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
if salario <= 1250.00:
    print(f'O salário de R${salario}, teve um aumento para R${(salario * 0.15) + salario:.2f}')
else:
    print(f'O salário de R${salario}, teve um aumento para R${(salario * 0.10) + salario:.2f}')
