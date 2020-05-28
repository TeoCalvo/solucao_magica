import pandas as pd
import sqlalchemy
from sklearn import tree
from sklearn import preprocessing
from sklearn import metrics

# Abre conecão com banco
dbpath = "/home/teo/Documentos/pessoais/projetos/ensino/projetos_twitch/maratona_ds/data/olist.db"
con = sqlalchemy.create_engine("sqlite:///"+dbpath)
con.table_names()

# Importa o modelo
modelpath = "/home/teo/Documentos/pessoais/projetos/ensino/projetos_twitch/maratona_ds/src/ep07/model_churn/models/arvore_decisao.pkl"
model = pd.read_pickle(modelpath)

# Importa os dados
df = pd.read_sql_table("tb_abt_churn", con)

df_onehot = pd.DataFrame(
    model['onehot'].transform( df[model['cat_features']] ),
    columns=model['onehot'].get_feature_names(model['cat_features'])
)

df_full = pd.concat( [df[model['num_features']], df_onehot], axis=1 )
df_full = df_full[ model['features_fit'] ]

df["proba"] = model["model"].predict_proba( df_full )[:,1]
df_analysis = df[['flag_churn', 'proba']].copy()

metrics.roc_auc_score( df_analysis["flag_churn"], df_analysis["proba"] )