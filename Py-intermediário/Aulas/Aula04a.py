# Treinando dicionários

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '3',
            'd': '2'
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 24 * 2?',
        'respostas': {
            'a': '10',
            'b': '26',
            'c': '48',
            'd': '56'
        },
        'resposta_certa': 'c',
    }
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolhas as opções abaixo:')
    for rk, rv in pv['respostas'].items():
        print(f'{rk}) {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('resposta correta!')
        respostas_certas += 1
    else:
        print('resposta incorreta.')
print(f'Você acertou {respostas_certas} questões!')
