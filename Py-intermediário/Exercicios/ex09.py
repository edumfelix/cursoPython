carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 25))

carrinhoSoma = sum([produto[1] for produto in carrinho])

print(carrinho)
print(f'Soma do carrinho = {carrinhoSoma}')
