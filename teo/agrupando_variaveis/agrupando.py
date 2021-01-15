import pandas as pd
import sqlalchemy
from sklearn import cluster
from sklearn.base import BaseEstimator, TransformerMixin

# Conexão com banco de dados
con = sqlalchemy.create_engine("sqlite:///" + "/home/teo/Documentos/pessoais/projetos/ensino/projetos_twitch/maratona_ds/data/olist.db" )

# Importou a base de dados
df = pd.read_sql_table( "tb_abt_churn", con )

# Definimos a variáveis categóricas
cat_features = df.dtypes[df.dtypes == 'object'].index.tolist()

# Tabela de frequencia das variáveis categóricas
pd.value_counts(df['seller_state'])

# Taxa da variável resposta em cada categoria
taxa_resposta = df.groupby( ['seller_state'] )[['flag_churn']].mean()

# Agrupamento das categortias com base na taxa de resposta
model = cluster.KMeans(n_clusters=6)
model.fit(taxa_resposta)
taxa_resposta["cluster_id"] = model.labels_
taxa_resposta["cluster_id"] = taxa_resposta["cluster_id"].astype(str)
taxa_resposta = taxa_resposta.rename(columns={"cluster_id":"seller_state_new"}).reset_index()
del taxa_resposta['flag_churn']
df = df.merge( taxa_resposta, on=['seller_state'] )

df.dtypes[df.dtypes=='object']

df.groupby(['seller_state'])[['flag_churn']].mean()

#Custom Transformer that extracts columns passed as argument to its constructor 
class ClassGroup(BaseEstimator, TransformerMixin):
    
    def __init__(self, feature_names, k=5):
        self._feature_names = feature_names
        self._new_feature_names = [f+"_new" for f in feature_names]
        self._k = k
        self._tables = {}
    
    def fit(self, X, y=None):
        for f in self._feature_names:
            df_tmp = self.group_one(X[f], y)
            self._tables[f] = df_tmp.rename(columns={"feature":f,
                                                     "cluster_id":f+"_new"})
        return self

    def transform(self, X, y=None):
        newX = X.copy()
        for f in self._feature_names:
            newX = newX.merge(self._tables[f], on=f)
        return newX[self._new_feature_names]

    def group_one(self, x, y):
        data = pd.DataFrame( {'feature':x,
                              'target':y} )
        summary = data.groupby(['feature'])[['target']].mean()
        model = cluster.KMeans(n_clusters=self._k, random_state=1992)
        model.fit(summary)
        summary['cluster_id'] = model.labels_
        summary = summary.reset_index()
        del summary['target']
        return summary

class_fit = ClassGroup( ['seller_city','seller_state'] )
class_fit.fit( df, df['flag_churn'] )
df_new = class_fit.transform( df )