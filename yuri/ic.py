import numpy as np
import random
import matplotlib.pyplot as plt

# Gera valores aleatório de uma população
mu = 31
num_aleatorio = np.random.normal(mu, 13,  size=5000)
pop = [ int(i) for i in num_aleatorio if i > 0 ]
print("A média da população é,", np.round(np.mean(pop),2), "anos de idade" )

plt.hist( pop )
plt.show()

# Gera uma amostra, vinda da população 

def gera_ic( pop, size ):
    amostra = np.random.choice( pop, size=size )
    x_barra = np.mean( amostra )
    s_2 = (np.std( amostra ) ** 2) * len(amostra) / (len(amostra) -1)
    ic = x_barra - 1.5 * np.sqrt(s_2 / len(amostra)), x_barra + 1.5 * np.sqrt(s_2 / len(amostra))
    return ic

test_ic = []
for i in range(100):
    ic = gera_ic( pop, 50 )
    if ic[0] <= mu <= ic[1]:
        test_ic.append(1)
    else:
        test_ic.append(0)

print( np.mean(test_ic) )