dicio = {
    'chave': 'valor',
}

print(dicio, type(dicio))
# Acessar valores
print(dicio['chave'])
print(dicio.get('chave'))

#Listar chaves
print(dicio.keys())

#Listar valoraoes
print(dicio.values())

#Retorna todos os itens do dicionario como tuplas em uma lista
print(dicio.items())

#Validação:
if "chave" in dicio:
    print("'chave' pertence à dicio")
