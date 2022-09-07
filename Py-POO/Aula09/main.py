from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('São Paulo', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('João', 45)
cliente2.insere_endereco('Belo Horizonte', 'MG')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Maria', 25)
cliente3.insere_endereco('Salvador', 'BA')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
