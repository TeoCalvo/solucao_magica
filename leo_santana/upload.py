import pandas as pd
import sqlalchemy

con = sqlalchemy.create_engine("sqlite:///leo_santana/dados.db")

i = 1
for chunk in pd.read_csv("leo_santana/votacao-zona.csv", chunksize=1000000):
    if i == 1:
        chunk.to_sql("tb_votacao", con, if_exists="replace")
    else:
        chunk.to_sql("tb_votacao", con, if_exists="append")
    i += 1
    print(i)