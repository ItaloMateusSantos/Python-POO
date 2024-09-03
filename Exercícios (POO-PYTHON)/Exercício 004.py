from abc import ABC,abstractmethod
import os
os.system('cls || clear')

class Funcionario(ABC):
#Método de inicialização, semlhando ao construto em Java________________
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario
    
    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
         BONIFICACAO = 1.2 #Equivalente a 20% de alguma coisa. 
         salario_final = self.salario * BONIFICACAO
         return salario_final

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh
    
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.1
        salrio_final = self.salario * BONIFICACAO
        return salrio_final
    # def calcular_salario(self) -> float:
    #     DESCONTO = 0.2
    #     salario_final = self.salario * DESCONTO
    #     return salario_final

gerente1 = Gerente('Marta', 25, 2000.0)
print(f'Nome: {gerente1.nome}')
print(f'Salário com acréscimo: R$ {gerente1.calcular_salario()}')

motoboy1 = Motoboy('Mario', 18, 1000.0, '123456')
print(f'Nome: {motoboy1.nome}')
print(f'Salário com desconto: R${motoboy1.calcular_salario()} ')