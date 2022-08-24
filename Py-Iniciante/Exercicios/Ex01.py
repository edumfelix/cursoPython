"""
    Faça um programa que peça ao usuário para digitar um número inteiro,
    informe se este número é par ou ímpar. Caso o usuário não digite um número
    inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

try:
    num = int(num)
except ValueError:
    print(f'Não foi possível representar o valor "{num}" para um número inteiro válido')
    exit(1)
if int(num) % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é impar')
