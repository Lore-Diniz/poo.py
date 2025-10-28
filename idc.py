
# 1. Associação: Pessoa e Livro

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livro = None  # Pessoa pode ter (ou não) um livro associado

    def ler(self, livro):
        self.livro = livro
        print(f"{self.nome} está lendo o livro '{livro.titulo}'.")


print("=== ASSOCIAÇÃO: PESSOA E LIVRO ===")
livro1 = Livro("A Revolução dos Bichos")
pessoa1 = Pessoa("Jefferson")
pessoa1.ler(livro1)

# 2. Associação via método: Aluno e Ônibus

class Onibus:
    def __init__(self, linha):
        self.linha = linha

    def transportar(self, aluno):
        print(f"O ônibus da linha {self.linha} está transportando o aluno {aluno.nome}.")


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def pegar_onibus(self, onibus):
        onibus.transportar(self)


print("\n=== ASSOCIAÇÃO: ALUNO E ÔNIBUS ===")
bus = Onibus("402 - Centro")
aluno1 = Aluno("Maria")
aluno1.pegar_onibus(bus)


# 3. Agregação: Departamento e Funcionários

class Funcionario:
    def __init__(self, nome):
        self.nome = nome


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []  # Armazena objetos já criados

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"Funcionários do departamento {self.nome}:")
        for f in self.funcionarios:
            print(f" - {f.nome}")


print("\n=== AGREGAÇÃO: DEPARTAMENTO E FUNCIONÁRIOS ===")
f1 = Funcionario("Antônio")
f2 = Funcionario("Clara")

dep = Departamento("Tecnologia da Informação")
dep.adicionar_funcionario(f1)
dep.adicionar_funcionario(f2)
dep.listar_funcionarios()

# 4. Agregação: Time e Jogador

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao


class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []  # Armazena jogadores já criados

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        print(f"Time {self.nome} - Jogadores:")
        for j in self.jogadores:
            print(f" - {j.nome} ({j.posicao})")


print("\n=== AGREGAÇÃO: TIME E JOGADOR ===")
j1 = Jogador("Carlos", "Goleiro")
j2 = Jogador("João", "Atacante")
time = Time("Leões do Xaréu")
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)
time.listar_jogadores()


# ==============================================
# 5. Composição: Carro e Motor
# ==============================================
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia}CV ligado.")


class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # Motor criado dentro do carro

    def ligar(self):
        print(f"O carro {self.modelo} está ligando...")
        self.motor.ligar()


print("\n=== COMPOSIÇÃO: CARRO E MOTOR ===")
carro = Carro("Fusca", 60)
carro.ligar()

print("Deletando o carro (e seu motor)...")
del carro
# Quando o carro deixa de existir, o motor também deixa (composição).


# ==============================================
# 6. Composição: Casa e Cômodos
# ==============================================
class Comodo:
    def __init__(self, nome):
        self.nome = nome


class Casa:
    def __init__(self):
        # Os cômodos são criados dentro da casa
        self.comodos = [Comodo("Sala"), Comodo("Cozinha"), Comodo("Quarto"), Comodo("Banheiro")]

    def mostrar_comodos(self):
        print("A casa possui os seguintes cômodos:")
        for c in self.comodos:
            print(f" - {c.nome}")


print("\n=== COMPOSIÇÃO: CASA E CÔMODOS ===")
casa = Casa()
casa.mostrar_comodos()

# ----------------------------------------------
# FIM DO CÓDIGO
# ----------------------------------------------
