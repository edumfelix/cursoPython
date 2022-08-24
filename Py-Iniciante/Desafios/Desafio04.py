# Gerar os últimos dois digitos e validar CPF

cpf = input('Digite um CPF: ')
novo_cpf = cpf[:-2]

#Formatando CPF em lista
cpfFormatado = [int(c) for c in str(novo_cpf)]

## Primeiro digito

#Preenchendo lista com valores comparados com exemplo do curso
listaCPF = []
for indice, cont in enumerate(range(10, 1, -1)):
    listaCPF.append(cpfFormatado[indice]*cont)

# Primeiro digito finalizado
primeiroDigito = 11 - (sum(listaCPF) % 11)

if primeiroDigito > 9:
    primeiroDigito = 0

cpfFormatado.append(primeiroDigito)

## Segundo digito
listaCPF.clear()
for indice, cont in enumerate(range(11, 1, -1)):
    listaCPF.append(cpfFormatado[indice]*cont)

# Segundo digito finalizado
segundoDigito = 11 - (sum(listaCPF) % 11)
cpfFormatado.append(segundoDigito)


novo_cpf = ''.join(map(str, cpfFormatado))
if novo_cpf == cpf:
    print('Válido.')

else:
    print('Inválido.')
