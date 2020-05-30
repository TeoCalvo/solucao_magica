import pandas as pd
import numpy as np
import sqlalchemy
from sklearn import tree
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt

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

def create_lift_table( y_true, proba, k ):
    percentis = np.linspace(0,100, int(100/k +1) )
    vl_percentis = np.percentile(proba, percentis)
    df_analysis["percentil"] = df_analysis["proba"].apply( lambda x: percentis[np.searchsorted( vl_percentis, x )] )
    tb_cutoff = df_analysis.groupby(["percentil"]).agg({"flag_churn":["count","sum", "mean"]})
    tb_cutoff.columns = tb_cutoff.columns.droplevel()
    tb_cutoff = tb_cutoff.reset_index().sort_values(by="percentil", ascending=False)

    tb_cutoff["cum_count"] = tb_cutoff["count"].cumsum()
    tb_cutoff["cum_sum"] = tb_cutoff["sum"].cumsum()
    tb_cutoff["cum_mean"] = tb_cutoff["cum_sum"] / tb_cutoff["cum_count"]

    tb_cutoff["gain"] = tb_cutoff["cum_mean"] / tb_cutoff["cum_mean"].min()
    tb_cutoff["tx_resposta"] = tb_cutoff["cum_sum"] / tb_cutoff["cum_sum"].max()

    return tb_cutoff

np.percentile( df["proba"], 80 )