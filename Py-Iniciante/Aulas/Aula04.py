"""
Formatando valores com modificadores

:s - Texto (str)
:d - Inteiros (int)
:f - Numeros de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d, ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 1
num2 = 3
divisao = num1 / num2
nome = 'Eduardo Felix'

print(f'{divisao:.2f}')
print(f'{nome:s}')
print(f'{num1:0<9}')
