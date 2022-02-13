# O mesmo professor do desafio anterior quer sortear o ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random

alunos = ['huguinho', 'zezinho', 'luizinho', 'joao']

random.shuffle(alunos)

print(alunos)
