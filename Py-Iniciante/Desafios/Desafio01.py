"""
*Criar variáveis para nome(str),idade(int),
*altura(float)epeso(float)de uma pessoa
*Criar variável comoano atual(int)
*Obteroano de nascimento da pessoa(baseado na idadeeno ano atual)
*ObteroIMC da pessoa com2casas decimais(pesoena altura da pessoa)
*Exibir um texto com todos os valores na tela usandoF-Strings(com as chaves)
"""

nome = 'Eduardo Felix'
idade = 18
altura = 1.76
peso = 80.1
ano = 2022
imc = peso / (altura ** 2)
anoNascimento = ano - idade

print(f'''Olá, {nome}! Você tem {idade} anos e nasceu no ano de {anoNascimento}. 
Você tem {altura}m de altura, pesa {peso}kg e seu imc é de {imc:.2f}.
''')
