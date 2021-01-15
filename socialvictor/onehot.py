import pandas as pd
from sklearn import preprocessing
import sqlalchemy

con = sqlalchemy.create_engine("sqlite:///" + "/home/teo/Documentos/pessoais/projetos/ensino/projetos_twitch/PandasToTeo/data/brasilio.db")

con.table_names()

df = pd.read_sql( "tb_candidatura", con )

columns_onehot = [ 'sigla_uf',
                   'descricao_cor_raca',
                   'descricao_estado_civil',
                   'descricao_genero',
                   'descricao_grau_instrucao' ]

df[columns_onehot]

onehot = preprocessing.OneHotEncoder(sparse=False, handle_unknown="ignore")
onehot.fit( df[columns_onehot] )

onehot_matrix = onehot.transform(df[columns_onehot])

df_onehot = pd.DataFrame( onehot_matrix, columns=onehot.get_feature_names( columns_onehot) )
df_onehot


df_new = df[ df['nome_urna'].apply( lambda x: "JAIR BOLSONARO" in x or "FERNANDO HADDAD" in x) ]

df_new_onehot = pd.DataFrame( onehot.transform( df_new[columns_onehot] ), columns=onehot.get_feature_names(columns_onehot))
