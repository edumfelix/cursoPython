# * Criar variáveis para nome(str), idade(int),
# * altura (float) e peso (float) de uma pessoa
# * Criar variável com o ano atual(int)
# * Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
# * Obter o IMC da pessoa com2casas decimais (peso e na altura da pessoa)
# * Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
altura = input('Digite sua altura: ')
peso = input('Digite seu peso: ')
anoAtual = 2022

#Validação dos dados recebidos
try:
    idade = int(idade)
    peso = float(peso)
    altura = float(altura)

except ValueError:
    print(f'Não foi possível representar o valor para um número válido')
    exit(1)

imc = peso / altura ** 2
nome = nome.title()

print(f'''{nome} tem {idade} anos, {altura:.2f}m de altura e pesa {peso:.1f}kg
O IMC de {nome} é {imc:.2f}.
{nome} nasceu em {anoAtual - idade}.
''')