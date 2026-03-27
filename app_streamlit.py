import streamlit as st
import predicao_lotofacil as api
import palpite_unico as analise
import filtro_estatistico as filtro
import abordagem_deterministica as determ
from datetime import datetime

# Configuração inicial da página
st.set_page_config(page_title="Preditor Lotofácil", page_icon="🎰", layout="centered")

st.title("🎰 Sistema de Predição Lotofácil")
st.markdown("---")
st.write("Este sistema analisa os dados históricos da API da Caixa e gera palpites baseados em 4 modelos diferentes.")

# Inicialização do estado da sessão para armazenar os palpites
if 'relatorio_texto' not in st.session_state:
    st.session_state.relatorio_texto = ""
if 'palpites_gerados' not in st.session_state:
    st.session_state.palpites_gerados = False

# Botão para gerar palpites
if st.button("🚀 Gerar Novos Palpites", use_container_width=True):
    with st.spinner("Buscando dados e processando modelos estatísticos..."):
        # 1. Coleta de Dados
        df_resultados = api.buscar_dados()
        
        if df_resultados is not None:
            # 2. Análise e Geração de Modelos
            resultado_analise = analise.analisar_tendencias(df_resultados)
            
            p_inteligente = analise.gerar_palpite_inteligente(resultado_analise)
            p_det = determ.palpite_deterministico(resultado_analise['Últimos 100 sorteios'])
            p_pesos = determ.gerarpalpite_com_pesos(resultado_analise)
            
            pool_freq = resultado_analise['Últimos 100 sorteios'].head(18).index.tolist()
            p_validado, tentativas = filtro.gerar_palpite_validado(pool_freq)
            
            # 3. Formatação do Relatório
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
            
            st.session_state.relatorio_texto = relatorio
            st.session_state.palpites_gerados = True
            st.success("Palpites gerados com sucesso!")
        else:
            st.error("Erro ao conectar com a API de resultados.")

# Área de exibição e Download
if st.session_state.palpites_gerados:
    st.subheader("📋 Palpites Calculados")
    st.code(st.session_state.relatorio_texto, language="text")
    
    st.download_button(
        label="💾 Gerar e Baixar Arquivo .txt",
        data=st.session_state.relatorio_texto,
        file_name=f"palpites_lotofacil_{datetime.now().strftime('%Y-%m-%d')}.txt",
        mime="text/plain",
        use_container_width=True
    )