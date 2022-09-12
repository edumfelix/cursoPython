# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR (.)

class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    # GETTER
    @property
    def nome(self):
        return 'Eduardo Felix'
    
    # @property
    # def sobrenome(self):
    #     return 'DESCONHECIDO'

    #SETTER
    @nome.setter
    def nome(self, nome):
        print('SETTER FOI EXECUTADO')
        self._nome = nome

p1 = Pessoa('Felix')

print(p1.nome)
print(p1.sobrenome)
