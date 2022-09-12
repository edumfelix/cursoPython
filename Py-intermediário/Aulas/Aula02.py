# Funções - def Python (part. 2)
# *args **kwargs
# ----------------------------------- #
# *args serve para quando o número de argumentos
# não estiver definido

def func(*args, **kwargs):
    print(args)
    print(kwargs)
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('idade not found!')


lista = [1, 2, 3, 4, 5]
func(*lista, nome='Eduardo', sobrenome='Felix', idade=18)
