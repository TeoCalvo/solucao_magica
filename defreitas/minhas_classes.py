class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Celular:
    def __init__(self, marca, modelo, dono:Pessoa, cor):
        self.marca = marca
        self.modelo = modelo
        self.dono = dono
        self.cor = cor
        self.lanterna = "off"

    def __repr__(self):
        return "-".join( [self.marca, self.modelo, self.dono] )

    def click_lanterna(self, cor='branco'):
        if self.lanterna == 'off':
            self.lanterna = "on"
            self.cor_lanterna = cor
        else:
            self.lanterna = "off"

class Automovel():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
    
    def acelerar(self, inc=1):
        self.velocidade+=inc

    def frear(self, dec=1):
        self.velocidade-=dec

class Onibus(Automovel):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.portas = 3
        self.acentos = 35
        self.rodas = 6

class Carro(Automovel):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.portas = 5
        self.acentos = 5
        self.rodas = 4

class Moto(Automovel):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.rodas = 2
        self.acentos = 2

cel_teo = Celular( "Xiomi", "Mi9 Lite", "Téo", "Branca")
cel_nah = Celular( "Xiomi", "Mi9 Lite", "Nah", "Branca")