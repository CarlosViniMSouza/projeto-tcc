import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

st.markdown("""
**Etapa 01:** Seleção do Dataset e das Ferramentas

1. Quanto ao dataset, o INPE fornece conjuntos de dados anuais em formato de Dados Abertos para acesso público. E por conta de problemas relacionados à estrutura dos arquivos .csv do INMET, os dados fornecidos pelo INPE serão o único dataset utilizado.
2. Quanto a parte ferramental, temos algumas bibliotecas para aplicar a parte metodológica: *Statistics; NumPy; SciPy; Pandas; Matplotlib;*

**Etapa 02:** Elaboração da Arquitetura e do Ambiente de Trabalho

1. Pesquisar sobre arquitetura para o trabalho.
2. Selecionar uma arquitetura e testar se é adequada.

**Etapa 03:** Amostragem

1. Coletar informações obtidas pertencentes ao dataset.
2. Amostragens a serem levadas em conta: 

&emsp; * *<u>Amostragem Probabilística:</u>* Amostragem aleatória simples; <br>
&emsp; * *<u>Amostragem Não Probabilística:</u>* Amostragem proposital; <br>

3. Links:

&emsp; * [Sampling with Python. Introduction | by Wendy Hu](https://medium.com/@whystudying/sampling-with-python-8bd135b3b078) <br>
&emsp; * [Sampling Methods - Types, Techniques and Examples (researchmethod.net)](https://researchmethod.net/sampling-methods/) <br>
&emsp; * [Sampling Distribution: Definition, Formula & Examples - Statistics By Jim](https://statisticsbyjim.com/hypothesis-testing/sampling-distribution/) <br>

**Etapa 04:** Tratamento dos Dados
1. Aplicar o conceito E.T.L. (*Extract, Transform, Load*) no dataset.
2. Selecionar/Criar uma classe para predição.
3. Exportar o dataset filtrado para próxima etapa.

**Etapa 05:** Estatística Descritiva
1. Coletar os resultados aguardados (médias, moda, mediana, variações, desvios, sazonalidade, quais padrões foram identificados, etc).
2. Organizar os resultados obtidos em uma tabela.
3. Links: 

&emsp; * [Python Statistics Fundamentals: How to Describe Your Data - Real Python](https://realpython.com/python-statistics/) <br>
&emsp; * [Master Statistical Analysis with Python: A Comprehensive Guide for Data Scientists](https://medium.com/illumination/how-to-perform-statistical-analysis-using-python-the-ultimate-guide-9458ae0ace1c) <br>

**Etapa 06:** Teste de Hipótese
1. Explorar possibilidades a serem usadas.
2. Exemplos teóricos a serem estudados: 

&emsp; * Teste de Shapiro-Wilk <br>
&emsp; * Coeficiente de Correlação de Pearson <br>
&emsp; * Teste de raiz unitária Dickey-Fuller aumentado <br>
&emsp; * Teste de Análise de Variância (*ANOVA - Analysis of Variance Test*) <br>
&emsp; * Teste de Friedman <br>

Links: [17 Statistical Hypothesis Tests in Python (Cheat Sheet) - MachineLearningMastery.com](https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/)

**Etapa 07:** Aplicação de Algoritmos preditivos

1. Estudar a forma como cada algoritmo selecionado opera, e se pode ser utilizado para predição da questão climática.
2. Comparar os resultados com a hipótese estatística elaborada anteriormente.
3. Links:

&emsp; * [Linear Algebra in Python: Matrix Inverses and Least Squares - Real Python](https://realpython.com/python-linear-algebra/) <br>
&emsp; * [Working With Linear Systems in Python With scipy.linalg - Real Python](https://realpython.com/python-scipy-linalg/#getting-started-with-scipylinalg) <br>

**Etapa 08:** Validação Algoritmos preditivos

1. Feito os estudos e os testes iniciais, fazer as equivalências para elaboração da Conclusão do Trabalho.
2. Empacotar e organizar os resultados para apresentação.
""", unsafe_allow_html=True)
