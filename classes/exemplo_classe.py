class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def retorna_dicionario(self):

            def gera_id_unico():
                import uuid

                return str(uuid.uuid4())

            return {
                'id': gera_id_unico(),
                'marca': self.marca,
                'modelo': self.modelo,
                'ano': self.ano
            }


carro = Carro('Fiat', 'Uno', 2010)
print(carro.retorna_dicionario())