class Passagem:

    def __init__(self, numero):
        self.numero = numero

    class Voo:
        def __init__(self, numero):
            self.numero = numero

        def valida_numero(self) -> bool:
            return self.numero != ''

    def valida_numero(self) -> bool:
        voo = self.Voo(self.numero)
        return voo.valida_numero()

passagem = Passagem('123')
print(passagem.valida_numero())

passagem = Passagem('')
print(passagem.valida_numero())