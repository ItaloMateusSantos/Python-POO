import os
from enum import Enum
os.system('cls || clear')

class Sexo(enumerate):
    MASCULINO = 'Masculino'
    FEMININO = 'Feminino'

class Pessoa:
#Equivalente ao Construtor do Java.
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
#Equivalente ao toString do Java.
        return (f'\nNome: {self.nome}'
                f'\nIdade: {self.idade}'
                )
    
pessoa_1 = Pessoa('Marta', 22, Sexo.FEMININO)

print(pessoa_1)
    

