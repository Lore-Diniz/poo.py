
from abc import ABC, abstractmethod

# 1. Criando uma interface Pagamento

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass


class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} no cartão de crédito.")


class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Gerando boleto no valor de R${valor:.2f}.")


print("=== TESTE INTERFACE PAGAMENTO ===")
cartao = CartaoCredito()
boleto = Boleto()

cartao.processar(150.00)
boleto.processar(200.00)



# 2. Interface múltipla (Ligavel e Desligavel)

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass


class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass


class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Computador ligado.")

    def desligar(self):
        print("Computador desligado.")


print("\n=== TESTE INTERFACES LIGAVEL/DESLIGAVEL ===")
pc = Computador()
pc.ligar()
pc.desligar()



# 3. Interface em herança múltipla

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass


class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass


class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("Imprimindo relatório...")

    def exportar(self):
        print("Exportando relatório em PDF.")


print("\n=== TESTE INTERFACES IMPRIMIVEL/EXPORTAVEL ===")
rel = Relatorio()
rel.imprimir()
rel.exportar()


# 4. Forçando contrato (erro ao não implementar tudo)

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass


# Classe que não implementa todos os métodos
class RepositorioMemoriaIncompleto(Repositorio):
    def salvar(self, objeto):
        print(f"Salvando objeto: {objeto}")


print("\n=== TESTE REPOSITORIO INCOMPLETO ===")
try:
    repo1 = RepositorioMemoriaIncompleto()
except TypeError as e:
    print("Erro:", e)


# Classe corrigida
class RepositorioMemoria(Repositorio):
    def __init__(self):
        self.dados = {}

    def salvar(self, objeto):
        novo_id = len(self.dados) + 1
        self.dados[novo_id] = objeto
        print(f"Objeto salvo com ID {novo_id}.")

    def buscar(self, id):
        return self.dados.get(id, "Objeto não encontrado.")


print("\n=== TESTE REPOSITORIO COMPLETO ===")
repo2 = RepositorioMemoria()
repo2.salvar("Usuário: Jefferson")
repo2.salvar("Usuário: Antônio")

print(repo2.buscar(1))
print(repo2.buscar(3))

# FIM DO CÓDIGO

