# Fazer uma calculadora

while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    operador = input('Digite o operador desejado: ')

#   Validação
    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número.')
        continue

#   Conversacao de tipos
    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(f'Resultado: {num1 + num2}')
    elif operador == '-':
        print(f'Resultado: {num1 - num2}')
    elif operador == '*':
        print(f'Resultado: {num1 * num2}')
    elif operador == '/':
        print(f'Resultado: {num1 / num2}')
    else:
        print('Operador inválido.')

    continuar = input('Deseja continuar?[s/n] ')
    if continuar == 'n' or 'N':
        break
    else:
        pass
