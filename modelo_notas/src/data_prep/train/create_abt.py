import os
import pandas as pd
import sqlalchemy
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--date_init", help="Data de incio para a extração da abt", default='2017-04-01')
parser.add_argument("--date_end", help="Data de fim para a extração da abt", default='2018-06-01')
args = parser.parse_args()

TRAIN_DIR = os.path.dirname( os.path.abspath( __file__ ) )
DATA_PREP_DIR = os.path.dirname(TRAIN_DIR)
SRC_DIR = os.path.dirname(DATA_PREP_DIR)
BASE_DIR  = os.path.dirname(SRC_DIR)

DB_PATH = "/run/media/data/teo/Documentos/pessoais/projetos/ensino/projetos_twitch/maratona_ds/data/olist.db"

# Leitura de um arquivo
with open( os.path.join(TRAIN_DIR, 'etl.sql'), 'r' ) as open_file:
    query = open_file.read()

query = query.format( dt_init=args.date_init,
                      dt_end=args.date_end  )

con = sqlalchemy.create_engine("sqlite:///" + DB_PATH)
for q in tqdm(query.split(";")[:-1]):
    con.execute(q)