"""
Encapsulamento
_   protected (public _)
__  private (_NOMECLASSE__nomeatributo)
"""

class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)
    
    def apaga_clientes(self, id):
        del self.dados['clientes'][id]
        print(f'Apagando {id}º id...')

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})


banco_de_dados = BaseDeDados()
banco_de_dados.inserir_clientes(1, 'Otávio')
banco_de_dados.inserir_clientes(2, 'Fábio')
banco_de_dados.inserir_clientes(3, 'Miranda')

banco_de_dados.lista_clientes()

banco_de_dados.apaga_clientes(2)

banco_de_dados.lista_clientes()
