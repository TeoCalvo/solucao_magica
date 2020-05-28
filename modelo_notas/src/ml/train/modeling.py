import os
import pandas as pd
import sqlalchemy

from sklearn import preprocessing
from sklearn import model_selection
from sklearn import tree
from sklearn import metrics

TRAIN_DIR = os.path.join( os.path.abspath( '.' ), 'src', 'ml','train' )
TRAIN_DIR = os.path.dirname( os.path.abspath( __file__ ) )
DATA_PREP_DIR = os.path.dirname(TRAIN_DIR)
SRC_DIR = os.path.dirname(DATA_PREP_DIR)
BASE_DIR  = os.path.dirname(SRC_DIR)

DB_PATH = "/run/media/data/teo/Documentos/pessoais/projetos/ensino/projetos_twitch/maratona_ds/data/olist.db"

# Conexao com sqlite
con = sqlalchemy.create_engine("sqlite:///"+DB_PATH)

# Importando dados...
abt = pd.read_sql_table("tb_abt_nota", con)

targets = ["nota_target","flag_nota_inc"]
target = "flag_nota_inc"
to_remove = ['dt_ref', 'seller_id', 'seller_city'] + targets
features = abt.columns.tolist()

for i in to_remove:
    features.remove(i)

cat_features = abt[features].dtypes[abt[features].dtypes=='object'].index.tolist()
num_features = list( set(features) - set(cat_features) )

X_train, X_test, y_train, y_test = model_selection.train_test_split(abt[features],
                                                                    abt[target],
                                                                    test_size=0.8,
                                                                    random_state=1992 )

X_train.reset_index(inplace=True)
X_test.reset_index(inplace=True)

onehot = preprocessing.OneHotEncoder(sparse=False, handle_unknown='ignore')
onehot.fit( X_train[cat_features] )
df_onehot = pd.DataFrame( onehot.transform( X_train[cat_features] ),
                          columns=onehot.get_feature_names(cat_features) )

X_train_full = pd.concat( [X_train[num_features], df_onehot], axis=1 )

clf = tree.DecisionTreeClassifier(min_samples_leaf=10)
clf.fit(X_train_full, y_train)

y_pred = clf.predict(X_train_full)
y_prob = clf.predict_proba(X_train_full)

metrics.accuracy_score(y_train, y_pred)
metrics.roc_auc_score(y_train, y_prob[:,1])