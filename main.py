import predicao_lotofacil as api
import palpite_unico as analise
import filtro_estatistico as filtro
import abordagem_deterministica as determ
from datetime import datetime

def executar_sistema():
    print("=== SISTEMA DE PREDIÇÃO LOTOFÁCIL INTEGRADO ===\n")

    # 1. Coleta de Dados (predicao_lotofacil.py)
    print("[1/4] Coletando dados históricos da API...")
    df_resultados = api.buscar_dados()
    
    if df_resultados is None:
        print("Erro: Não foi possível obter os dados da API.")
        return

    # 2. Análise de Tendências (palpite_unico.py)
    print("[2/4] Analisando frequências de dezenas...")
    resultado_analise = analise.analisar_tendencias(df_resultados)

    # 3. Geração de Modelos (Integração de múltiplos arquivos)
    print("[3/4] Calculando modelos de predição...")

    # Modelo 1: Inteligente (10 quentes + 5 frios de palpite_unico.py)
    p_inteligente = analise.gerar_palpite_inteligente(resultado_analise)

    # Modelo 2: Determinístico (Top 15 frequentes de abordagem_deterministica.py)
    p_det = determ.palpite_deterministico(resultado_analise['Últimos 100 sorteios'])

    # Modelo 3: Probabilístico (Amostragem por peso de abordagem_deterministica.py)
    p_pesos = determ.gerarpalpite_com_pesos(resultado_analise)

    # Modelo 4: Estatístico Validado (Filtros técnicos de filtro_estatistico.py)
    # Usamos um pool dos 18 números mais frequentes para maior assertividade
    pool_frequencia = resultado_analise['Últimos 100 sorteios'].head(18).index.tolist()
    p_validado, tentativas = filtro.gerar_palpite_validado(pool_frequencia)

    # 4. Apresentação das Respostas
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nome_arquivo = f"palpites_{datetime.now().strftime('%Y-%m-%d')}.txt"

    relatorio = (
        f"{'='*65}\n"
        f"{'RELATÓRIO DE PALPITES GERADOS - ' + data_hora:^65}\n"
        f"{'='*65}\n"
        f"A. MODELO INTELIGENTE (Hot/Cold):  {p_inteligente}\n"
        f"B. MODELO DETERMINÍSTICO (Top):    {p_det}\n"
        f"C. MODELO PROBABILÍSTICO (Pesos):  {p_pesos}\n"
        f"D. MODELO FILTRADO (Estatístico):  {p_validado} ({tentativas} tentativas)\n"
        f"{'='*65}\n"
    )

    print("\n" + relatorio)

    # Salvando em arquivo com codificação UTF-8 para evitar problemas de caracteres
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(relatorio)
    print(f"Relatório exportado com sucesso para: {nome_arquivo}")

if __name__ == "__main__":
    executar_sistema()
