import random

def validar_soma(dezenas):
    soma = sum(dezenas)
    return 180 <= soma <= 200

def validar_paridade(dezenas):
    pares = sum(1 for d in dezenas if d % 2 == 0)

    return pares in [7, 8]

def validar_primos(dezenas):
    primos_lotofacil = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    contagem_primos = len([n for n in dezenas if n in primos_lotofacil])
    return 5 <= contagem_primos <= 6

def gerar_palpite_validado(pesos_numeros, max_tentativas=10000, callback_progresso=None):
    tentativas = 0
    # Se não houver pesos, usa todos os números de 1 a 25
    pool = pesos_numeros if pesos_numeros else list(range(1, 26))
    
    while True:
        tentativas += 1

        # Atualiza a interface a cada 100 tentativas para manter a performance
        if callback_progresso and tentativas % 100 == 0:
            callback_progresso(tentativas, max_tentativas)
        
        # Se exceder o limite, expande o pool para todos os números para evitar loop infinito
        if tentativas > max_tentativas and pool != list(range(1, 26)):
            pool = list(range(1, 26))
            continue

        palpite = sorted(random.sample(pool, 15))
        if validar_soma(palpite) and validar_paridade(palpite) and validar_primos(palpite):
            return palpite, tentativas