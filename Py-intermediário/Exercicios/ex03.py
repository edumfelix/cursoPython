# Crie uma função que receba 2 números. O primeiro
# é um valor e o segundo um percentual (ex. 10%). Retorne
# (return) o valor do primeiro número somado do aumento
# do percentual

def somaPercentual(n1, n2):

    return n1 + (n1*n2)


a = int(input('Digite um número inteiro: '))
b = int(input('Digite um valor em %: '))
b = b/100

print(somaPercentual(a, b))
