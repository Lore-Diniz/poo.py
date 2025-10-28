
# EXERCÍCIOS SOBRE CLASSES ABSTRATAS EM PYTHON

from abc import ABC, abstractmethod

# 1. Classe abstrata Animal

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass


# Classes concretas que implementam o método abstrato
class Cachorro(Animal):
    def falar(self):
        return "Au au!"


class Gato(Animal):
    def falar(self):
        return "Miau!"


# Teste de uso
print("=== TESTE CLASSE ANIMAL ===")
dog = Cachorro()
cat = Gato()

print(dog.falar())  # Saída: Au au!
print(cat.falar())  # Saída: Miau!


# 2. Tentativa de instanciar classe abstrata

print("\n=== TESTE DE INSTANCIAÇÃO PROIBIDA ===")
try:
    animal = Animal()  # Isso gera erro
except TypeError as e:
    print("Erro:", e)


# 3. Classe abstrata com múltiplos métodos

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


# Teste de uso
print("\n=== TESTE CLASSE RETANGULO ===")
ret = Retangulo(5, 3)
print("Área:", ret.area())          # Saída: 15
print("Perímetro:", ret.perimetro())  # Saída: 16

# 4. Classe abstrata com método abstrato não implementado

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass


# Classe que implementa apenas um método abstrato
class CarroIncompleto(Transporte):
    def mover(self):
        print("O carro está em movimento.")


print("\n=== TESTE CLASSE CARRO INCOMPLETO ===")
try:
    carro1 = CarroIncompleto()  # Isso gera erro
except TypeError as e:
    print("Erro:", e)


# Classe corrigida
class Carro(Transporte):
    def mover(self):
        print("O carro está em movimento.")

    def parar(self):
        print("O carro parou.")


# Teste de uso
print("\n=== TESTE CLASSE CARRO COMPLETO ===")
carro2 = Carro()
carro2.mover()
carro2.parar()

# ----------------------------------------------

