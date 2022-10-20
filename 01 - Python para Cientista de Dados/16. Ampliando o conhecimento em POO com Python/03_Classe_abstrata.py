from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty


class ControleRemoto(ABC):
  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

  @property
  @abstractproperty
  def marca(self):
    pass

class ControleTV(ControleRemoto):
  def ligar(self):
    print("Ligando a TV...")
    print("Ligada!")

  def desligar(self):
    print("Desligando a TV ...")
    print("Desligada!")

  @property
  def marca(self):
    return "LG"

class ControleArCondicionado(ControleRemoto):
  def ligar(self):
    print("Ligando a ar condicionado...")
    print("Ligada!")

  def desligar(self):
    print("Desligando a ar condicionado ...")
    print("Desligada!")

  @property
  def marca(self):
    return "Samsung"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)