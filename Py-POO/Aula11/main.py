# Classes Abstratas
# Tipo de classe especial que não pode ser instanciada, apenas pode ser herdada

from abc import ABC, abstractmethod

class A(ABC):
  @abstractmethod
  def falar(self):
    pass

class B(A):
  def falar(self):
    print('Falando... B...')

a = B()
a.falar()
