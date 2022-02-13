# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido
import random

alunos = ['huguinho', 'zezinho', 'luizinho', 'joao']

apagar = random.choice(alunos)

print(f'Quem irá apagar hoje é o {apagar.capitalize()}')
