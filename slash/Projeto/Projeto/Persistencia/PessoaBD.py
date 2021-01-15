from Projeto.Modelo import Pessoa
import sqlite3
print("oi")
bancoDeDados = 'pessoa.bd'

class PessoaBD():

    def __init__(self):
        with sqlite3.connect(bancoDeDados)as banco:
            banco.execute('''create table if not exist pessoa(
                id integer not null primary key autoincrement,
                nomeCompleto text not null,
                email text not null,
                escolaridade text not null)''')

    def incluir(self, pessoa):
        with sqlite3.connect(bancoDeDados) as banco:
            cursor= banco.cursor()
            cursor.exeute(''' insert into pessoa(nomeCompleto, email, senha, escolaridade)
            values(?,?,?,?)''',[pessoa.nomeCompleto, pessoa.email, pessoa.senha, pessoa.escolaridade])

            pessoa.id=cursor.lastrowid

    def alterar(self, pessoa):
        with sqlite3.connect(bancoDeDados) as banco:
            banco.execute('''update pessoa set nomeCompleto = ?, email = ?,
            senha = ?, escolaridade = ? where id = ?''',[pessoa.nomeCompleto,
            pessoa.email, pessoa.senha, pessoa.escolaridade, pessoa.id])

    def excluir(self, id):
        with sqlite3.connect(bancoDeDados) as banco:
            banco.execute('delete from pessoa where id = ?',[id])


    def consultar(self, id=None):
        '''Se um código for passado como parametro, o método consultar
        tenta devolver uma unia pessoa se esse ID existir na tabela
        Caso id seja None, entao o metodo consultar ira devolver uma lista 
        com todas as pessoas
        '''
        with sqlite3.connect(bancoDeDados) as banco:
            if id:
                dados = banco.execute('''Select id,nomeCompleto,email,senha,esolaridade
                from pessoa
                where id = ?''',[id])
                dados = dados.fetchone() #extraimos a coluna das consulta
                if dados:
                    resultado = Pessoa(dados[0],dados[1],dados[2],dados[3],dados[4])
                    return resultado
            else:
                listaPessoas = []
                dados = banco.execute('Selet id,nomeCompleto,email,senha,escolaridade from pessoa')
                dados = dados.fetchall()
                for linha in dados:
                    p = Pessoa(linha[0],linha[1],linha[2],linha[3],linha[4])
                    listaPessoas.append(p)
                return listaPessoas
