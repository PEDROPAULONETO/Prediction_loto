import numpy as np
import pandas as pd

def palpite_deterministico(df_frequencia):
    # Regra fixa: Pegamos os 15 números mais frequentes da janela de 100 sorteios
    palpite = df_frequencia.head(15).index.tolist()  # Pegamos os 15 números mais frequentes dos últimos 100 sorteios
    return sorted(palpite)

def gerarpalpite_com_pesos(analise_frequencia):
    # Transforma a porcentagem de frequência em probabilidade (pesos)
    f_100 = analise_frequencia['Últimos 100 sorteios']
    pesos = f_100 / f_100.sum() # Normaliza para que a soma seja 1
    numeros = f_100.index.tolist()
    
    palpite = np.random.choice(numeros, size=15, replace=False, p=pesos)
    return sorted(palpite.tolist())