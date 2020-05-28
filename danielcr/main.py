import pandas as pd

genero = pd.read_excel( "generofilmes.xlsx" )
cinema = pd.read_excel( "cinemasabado.xlsx")

# Serie de genero
genero_raiz = genero.set_index("FILME")["GENERO"]

# Serie de cinema
ingressos_raiz = cinema.set_index("FILME")["INGRESSOS"]

# Definie o novo index da série maldita
ingressos_genero = ingressos_raiz.copy()
ingressos_genero.index = [genero_raiz[i] for i in ingressos_raiz.index]

# Soma a caralha por genero:
print(ingressos_genero.sum(level=0))

# Média de ingressos por filme
ingressos_raiz.mean(level=0)

# Melhor jeito
df_full = cinema.merge(genero, on="FILME" ) # LEFT FUCKING JOIN
df_full.groupby("GENERO")["INGRESSOS"].sum()