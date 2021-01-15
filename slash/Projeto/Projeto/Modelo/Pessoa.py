class Pessoa():
    def __init__(self, id=None, nomeCompleto='vazio', email='vazio',senha='vazio',escolaridade='vazio'):
        self.__id=id
        self.__nomeCompleto = nomeCompleto
        self.__email = email
        self.__senha = senha
        self.__escolaridade = escolaridade
    #get a set id
    @property
    def id(self):
        return self.__id


    @id.setter
    def id(self, valor):
        self.__id = valor

    @property
    def nomeCompleto(self):
        return self.__nomeCompleto


    @nomeCompleto.setter
    def nomeCompleto(self, valor):
        self.__nomeCompleto = valor

    @property
    def email(self):
        return self.__email


    @email.setter
    def email(self, valor):
        self.__email = valor


    @property
    def senha(self):
        return self.__senha


    @senha.setter
    def senha(self, valor):
        self.__senha = valor

    @property
    def escolaridade(self):
        return self.__escolaridade


    @escolaridade.setter
    def escolaridade(self, valor):
        self.__escolaridade = valor



