# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('O segundo: '))
n3 = int(input('Agora o terceiro: '))
print('Testando alguns tipos de casos')

print('If or Else ordem:')
print('-'*20)
if n1 > n2 and n1 > n3:
    if n2 < n1 and n2 < n3:
        print(f'O numero {n1} é maior, {n2} é menor')
    else:
        print(f'O numero {n1} é maior, {n3} é menor')
elif n2 > n1 and n2 > n3:
    if n1 < n2 and n1 < n3:
        print(f'O numero {n2} é maior, {n1} é menor')
    else:
        print(f'O numero {n2} é maior, {n3} é menor')
else:
    if n2 < n1:
        print(f'O numero {n3} é maior, {n2} é menor')
    else:
        print(f'O numero {n3} é maior, {n1} é menor')
print('-'*20)
print('Pegando o menor valor substituindo o valor da variavel menor:')
print('-'*20)
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'Variavel menor é {menor}')
print('-'*20)
print('Pegando o maior valor substituindo o valor da variavel maior:')
print('-'*20)
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'Variavel maior é {maior}')
print('-'*20)
# ou
print('-'*20)
print('Sorted List ordem:')
print('-'*20)
lista = [n1, n2, n3]
lista_ordem = sorted(lista)
print(f'O numero {lista_ordem[-1]} é maior, {lista_ordem[0]} é menor')

# ou
print('-'*20)
print('Min Max List ordem:')
print('-'*20)
print(f'O numero {max(lista_ordem)} é maior, {min(lista_ordem)} é menor')
