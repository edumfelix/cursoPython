"""
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
    descrito, exiba a saudação apropriada. Ex.
    Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = int(input('Que horas são? '))

if 11 >= horas >= 0:
    print('Bom dia!')
elif 17 >= horas >= 12:
    print('Boa tarde!')
else:
    print('Boa noite!')