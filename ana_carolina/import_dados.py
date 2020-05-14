import pandas as pd
import numpy as np
import datetime

time_init = datetime.datetime.now()
# Endereço do arquivo
endereco_arquivo = '/home/teo/Documentos/pessoais/projetos/ensino/projetos_twitch/solucao_magica/ana_carolina/entrada.txt'

# Leitura do arquivo
dados = pd.read_csv( endereco_arquivo, sep=' ', header=None)

# Colunas do arquivo
dados.columns = ['fornecedor', 'mes_inicio', 'mes_final', 'valor']

# Filtro para fornecedor
dados[ dados['fornecedor'] == 1 ].head()

# Convertendo para matriz
dados = dados.values

#Linhas onde fornecedor é igual a 1

# Coluna de mes de início
dados[:,1]

# Coluna mes de ínicio igual a 1 => True e False
dados[:,2] == 3

# Fornecedor mes inicio = 1
dados[dados[:,1] == 1 ,:]

# Filtro de duas colunas
dados[ (dados[:,1] == 1) & (dados[:, 2] == 1) , :]

def filtro_mes( dados, mes_init, mes_fim ):
    ''' Definição da função para aplicar o filtro'''
    return dados[ (dados[:, 1]==mes_init) & (dados[:, 2]==mes_fim) , :]

# Uso da função
filtro_mes( dados, 1, 12 )
time_end = datetime.datetime.now()

print(time_end - time_init)