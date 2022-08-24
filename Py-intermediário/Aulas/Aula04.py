# Dicionários

clientes = {
    'cliente1': {
        'nome':  'Eduardo',
        'sobrenome': 'Felix'
    },
    'cliente2': {
        'nome':  'Maria',
        'sobrenome': 'Eduarda'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
