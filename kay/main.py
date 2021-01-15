import pandas as pd

df = pd.read_csv("dado.csv")

df['unit'] = 1
df['unit'] = df.groupby(["id"]).cumsum()
df_new = df.set_index( ['id', 'unit'] ).unstack(level=-1)

df_new.columns = df_new.columns.droplevel()
df_new.reset_index(inplace=True)

df_final = pd.DataFrame()
df_final[df_new.columns] = df_new
