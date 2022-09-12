# Fizz Buzz - Se o parâmetro da função for divisível
# por 2, retorne fizz, se o parâmetro da função for
# divisível por 5 retorne buzz. Se o parâmetro da
# função for divisível por 5 e por 3, retorne FizzBuzz,
# caso contrário, retorne número enviado.

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz'
    elif num % 2 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    else:
        return num


num = int(input('Digite um número inteiro: '))
print(fizzbuzz(num))
