from abc import ABC, abstractmethod
import os
os.system('cls || clear')

class Funcionario(ABC):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def Endereco(Funcionario):
        def salario_final(selfe) -> float:

