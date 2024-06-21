import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()

show_pages(
    [   
        Page("./streamlit_app.py", "Projeto de Pesquisa para TCC", "💻"),

        Section("TCC I", "✅"),
        Page("./src/pages/Datasets.py", "Datasets", icon="💾", in_section=True),
        Page("./src/pages/Architecture.py", "Arquitetura", "📜", in_section=True),
        Page("./src/pages/StepsSearch.py", "EtapasDaPesquisa", "📑", in_section=True),
        Page("./src/pages/DataSampling.py", "Amostragem", icon="📈", in_section=True),
        Page("./src/pages/DataProcessing.py", "TratamentoDosDados", icon="🎲", in_section=True),
        Page("./src/pages/StatisticDescritive.py", "EstatisticaDescritiva", icon="📊", in_section=True),
        Page("./src/pages/HypothesisTest.py", "TestesDeHipotese", icon="🔎", in_section=True),

        Section("TCC II", "⌛"),
        Page("./src/pages/MLSerialTimesForecasting.py", "MLPredicaoEmSerieTemporal", icon="🕜", in_section=True),
        Page("./src/pages/Conclusions.py", "Conclusoes", icon="⚖️", in_section=True),
    ]
)

st.markdown("""
INTEGRAÇÃO DE ANÁLISE EXPLORATÓRIA E PREVISÃO DE MACHINE LEARNING EM SÉRIES TEMPORAIS DE QUEIMADAS NA AMAZÔNIA LEGAL: 
ESTRATÉGIAS PARA O GERENCIAMENTO PROATIVO DE RISCOS AMBIENTAIS

---

O estudo dirigido neste artigo visa pôr em teste metodologias convencionais, como técnicas exploratórias de análise em dados massivos, métodos estatísticos comuns (tais como Estatística Descritiva, Amostragem, Testes de Hipótese), além de procurar possíveis padrões comportamentais nos dados disponibilizados nas referidas fontes na pesquisa. No qual foram utilizadas ferramentas de análise de dados, bancos disponíveis por plataformas de Dados Abertos, de organizações e instituições públicas, métodos estatísticos e de análise exploratória para pesquisas desse porte. Permitindo uma visualização mais abrangente dos focos de queimadas na região da Floresta Amazônica Brasileira, e maior compreensão sobre essas ocorrências.

`Palavras-chave: Queimadas, Floresta Amazônica, Análise de Dados, Análise Exploratória, Dados Geoespaciais`

---

*The study conducted in this article aims to test conventional methodologies, such as exploratory analysis techniques on massive data, common statistical methods (such as Descriptive Statistics, Sampling, Hypothesis Testing), in addition to looking for possible behavioral patterns in the data available in the aforementioned sources in search. In which data analysis tools were used, databases available through Open Data platforms, from organizations and public institutions, statistical and exploratory analysis methods for research of this size. Allowing a more comprehensive view of fire outbreaks in the Brazilian Amazon Forest region, and greater understanding of these occurrences.*

`Keywords: Burns, Amazon Forest, Data Analysis, Exploratory Analysis, Geospatial Data`
""", unsafe_allow_html=True)

st.markdown("---")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
