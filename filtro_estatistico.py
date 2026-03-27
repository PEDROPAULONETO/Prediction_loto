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

def gerar_palpite_validado(pesos_numeros):
    tentativas = 0
    # Se não houver pesos, usa todos os números de 1 a 25
    pool = pesos_numeros if pesos_numeros else list(range(1, 26))
    
    while True:
        tentativas += 1
        palpite = sorted(random.sample(pool, 15))
        if validar_soma(palpite) and validar_paridade(palpite) and validar_primos(palpite):
            return palpite, tentativas