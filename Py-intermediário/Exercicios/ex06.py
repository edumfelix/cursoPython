# Crie uma função1 que recebe uma função2 como
# parâmetro e retorne o valor da função2 executada.
# Faça a função1 executar duas funções que recebam um
# número diferente de argumentos

def func1(a, b):
    return a + '\n' + f'Você tem {2022 - int(b)} anos.'

def saudacao(nome):
    return f'Oi {nome}. Bom dia!'


def idade(idadeUsuario):
    return idadeUsuario


nome = input('Digite seu nome: ')
idadeUsuario = input('Em que ano você nasceu? ')

print(func1(saudacao(nome), idade(idadeUsuario)))
