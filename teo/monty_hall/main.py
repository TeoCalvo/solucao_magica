import random
import pandas as pd

def monty_hall():
        
    items = ["macaco", "burro", "carro"]
    random.shuffle(items)
    portas = {1:items[0], 2:items[1], 3:items[2],}

    # O jogo começa aqui
    escolha = set([random.randint(1,3)])
    premio = set([i for i in portas if portas[i]=="carro"])
    abertura = set([random.choice(list(set(portas.keys()) - escolha - premio))])
    nova_escolha = set([random.choice(list(set(portas.keys()) - abertura))])

    if escolha == nova_escolha:
        trocou = 0
    else:
        trocou = 1

    if nova_escolha == premio:
        ganhou = 1
    else:
        ganhou = 0

    return trocou, ganhou

def ite_run(n = 10000):

    trocas = []
    ganhos = []

    for i in range(n):
        t, g = monty_hall()
        trocas.append(t)
        ganhos.append(g)
    
    return pd.DataFrame( {"trocas": trocas, "ganhos":ganhos} )


df = ite_run()
