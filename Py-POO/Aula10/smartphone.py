from classes import Eletronico

class Smartphone(Eletronico):
  def __init__(self, nome):
    super().__init__(nome)
    self._conectado = False
    self.conectado = True

  def conectar(self):
    if not self._ligado:
      print(f'{self._nome} não está ligado.')
      return

    if self._conectado:
      print(f'{self._nome} já está conectado.')
      return
    
    self.conectado = False

  def desconectar(self):
    if not self._conectado:
      print(f'{self._nome} Não está conectado.')
      return
    self._conectado = False