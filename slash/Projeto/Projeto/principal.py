from Projeto.Modelo.Pessoa import Pessoa
from Projeto.Persistencia.PessoaBD import PessoaBD

pessoa1 = Pessoa(None,'Renato','renato@gmail.br','123456','superior')

pesBD = PessoaBD()
pesBD.incluir(pessoa1)
print(pessoa1.id)

for pessoa in pesBD.consultar():
    print(pessoa.nomeCompleto)