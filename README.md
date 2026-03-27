# 🎰 Sistema de Predição Lotofácil

Este projeto é uma ferramenta de análise estatística e geração de palpites para a Lotofácil, utilizando dados históricos reais extraídos via API. O sistema processa as tendências de sorteios anteriores e aplica modelos matemáticos e filtros probabilísticos para sugerir jogos com maior embasamento técnico.

## 🚀 Tecnologias Utilizadas

*   **Python 3.x**: Linguagem principal do projeto.
*   **Pandas**: Manipulação de dados e cálculos de frequência de dezenas.
*   **NumPy**: Processamento numérico para geração de escolhas ponderadas.
*   **Streamlit**: Interface web interativa para visualização dos resultados.
*   **Requests**: Consumo da API de resultados da Caixa Econômica Federal.

## 📊 Modelos de Predição

O sistema utiliza quatro abordagens distintas para a geração de palpites:

1.  **Modelo Inteligente (Hot/Cold):**
    *   Baseia-se na teoria de tendências. Seleciona as 10 dezenas mais frequentes ("quentes") e as 5 menos frequentes ("frias") de uma janela específica de sorteios (últimos 50).
2.  **Modelo Determinístico (Top):**
    *   Uma abordagem puramente estatística que seleciona as 15 dezenas com maior incidência histórica nos últimos 100 concursos.
3.  **Modelo Probabilístico (Pesos):**
    *   Utiliza a frequência relativa de cada número como peso para um sorteio aleatório ponderado. Números que saem mais vezes têm uma probabilidade matematicamente maior de serem selecionados no palpite.
4.  **Modelo Filtrado (Estatístico Validado):**
    *   Gera combinações a partir dos 18 números mais frequentes e as submete a rigorosos filtros estatísticos baseados em padrões históricos da Lotofácil (veja abaixo).

## ⚙️ Filtros Estatísticos Aplicados

Para aumentar a qualidade dos palpites (especialmente no Modelo Filtrado), o sistema valida se a combinação atende a critérios técnicos:

*   **Soma das Dezenas:** A soma total dos números selecionados deve estar entre **180 e 200**. Este intervalo concentra a grande maioria dos resultados reais.
*   **Paridade:** O palpite deve conter obrigatoriamente **7 ou 8 números pares**, mantendo o equilíbrio comum nos sorteios oficiais.
*   **Números Primos:** Validação para garantir a presença de **5 ou 6 números primos** (2, 3, 5, 7, 11, 13, 17, 19, 23), seguindo a distribuição de probabilidade da modalidade.

## 📂 Estrutura do Projeto

*   `main.py`: Interface de linha de comando (CLI) para execução 
*   `app_streamlit.py`: Dashboard interativo para uso via navegador.
*   `predicao_lotofacil.py`: Módulo de integração com a API de dados.
direta.
*   `palpite_unico.py`: Lógica de análise de tendências e modelo Hot/Cold.
*   `abordagem_deterministica.py`: Lógica para modelos de frequência e pesos.
*   `filtro_estatistico.py`: Motor de validação de regras matemáticas.

## 🛠️ Como Executar

1.  Instale as dependências:
    ```bash
    pip install pandas numpy requests streamlit
    ```
2.  Execute a versão Web:
    ```bash
    streamlit run app_streamlit.py
    ```
    *Ou a versão CLI:*
    ```bash
    python main.py
    ```

---
**Aviso Legal:** Este sistema é uma ferramenta de estudo estatístico e não garante ganhos financeiros. Loterias são jogos de azar e os resultados são independentes.

*Desenvolvido para fins de análise de dados e aprendizado em engenharia de software.*