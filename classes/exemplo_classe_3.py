class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos, {self.altura}m de altura e pesa {self.peso}kg'

params = {
    'nome': 'João',
    'idade': 25,
    'altura': 1.75,
    'peso': 80.0
}

pessoa = Pessoa(**params)

print(pessoa)