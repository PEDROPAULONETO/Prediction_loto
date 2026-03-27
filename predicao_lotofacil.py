import pandas as pd
import requests

def buscar_dados():

    url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        # Converte as dezenas de string para inteiro para permitir cálculos matemáticos
        df['dezenas'] = df['dezenas'].apply(lambda x: [int(n) for n in x])
        return df
    else:
        print("Erro ao buscar os dados:")
        return None