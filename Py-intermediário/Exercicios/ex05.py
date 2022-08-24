# Crie uma função 1 que recebe uma função2 como parâmetro
# e retorne o valor da função 2 executada

def func1(a):
    return a


def func2():
    return 'Hello, world!'


print(func1(func2()))
