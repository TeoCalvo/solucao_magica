import pandas as pd
import sqlalchemy
import os

from sklearn import preprocessing
from sklearn import decomposition

BASE_DIR = os.path.join( os.path.abspath( '.' ), 'nocky')
BASE_DIR = os.path.dirname( os.path.abspath( __file__ ) )
DB_PATH = os.path.join( BASE_DIR, 'olist.db' )

def import_query( path, **kwargs ):
    with open( path, 'r', **kwargs ) as file_open:
        result = file_open.read()
    return result

# Abre conexão com banco de dados
engine = sqlalchemy.create_engine( "sqlite:///" + DB_PATH )

# Importa a query
query = import_query( os.path.join( BASE_DIR, 'query_1.sql' ) )

# Executa query e retorna um dataframe
df = pd.read_sql_query( query, engine )

num_columns = df.dtypes[df.dtypes != 'object'].index.tolist()
cat_columns = df.dtypes[df.dtypes == 'object'].index.tolist()
cat_columns.remove('seller_id')

# treina o onehot
onehot = preprocessing.OneHotEncoder(sparse=False, handle_unknown='ignore')
onehot.fit( df[ cat_columns ] )

# Transforma o dado original em onehot
onehot_df = pd.DataFrame( onehot.transform( df[ cat_columns ] ),
                          columns=onehot.get_feature_names( cat_columns ) )

# junta das bases
df_final = pd.concat( [df[num_columns], onehot_df], axis=1  )

# Treina PCA
pca = decomposition.PCA(n_components=5)
pca.fit( df_final )

# Aplica o PCA
df_pcs = pd.DataFrame( pca.transform(df_final) )

