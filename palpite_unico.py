import pandas as pd

def analisar_tendencias(df, janelas = [10, 50, 100]):
    analise = pd.DataFrame()
    # Extrai a lista de dezenas (assumindo que a coluna se chama 'dezenas')
    todos_sorteios = df['dezenas'].tolist()

    for janela in janelas:
        ultimos = todos_sorteios[:janela]
        flat_list = [item for sublist in ultimos for item in sublist]
        frequencia =  pd.Series(flat_list).value_counts(normalize=True) * 100
        analise[f'Últimos {janela} sorteios'] = frequencia

    return analise

def gerar_palpite_inteligente(analise_frequencia):

    f_atual = analise_frequencia['Últimos 50 sorteios']
    quentes = f_atual.head(10).index.tolist()
    frios = f_atual.tail(5).index.tolist()

    palpite = sorted(quentes + frios)

    return palpite