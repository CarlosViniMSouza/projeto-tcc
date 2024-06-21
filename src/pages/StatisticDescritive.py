import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

st.markdown("""
A Estatística Descritiva é um ramo da ciência estatística que tem por propósito a descrição dos dados em questão, ou seja, converter dados em informação a ser explorada pelo pesquisador. Empregada para identificar características particulares, tais como média, desvio padrão, porcentagens, taxas, contagens e intervalo, etc. 
A Estatística Descritiva simplesmente descreve os dados da forma como são, mas sem generalização. (Dias et al., 2019; [FROST, Jim](https://statisticsbyjim.com/glossary/descriptive-statistics/)). 

Essa parte da pesquisa foi dividida em 3 etapas:

1. **Informações básicas com Numpy e Pandas:** local de obtenção das médias, modas, medianas, variâncias, desvios-padrão, tipo de dados das colunas, quantidade de dados, etc.
2. **Visualização de Dados com Matplotlib (básico):** informações primárias a serem obtidas isoladamente, tais como as incidências de queimadas nos estados; os municípios com mais registros de focos, e correlações entre classes com Mapa de Calor.
3. **Visualização de Dados com Plotly (avançado):** além das informações básicas, insights mais difíceis e mais elaborados foram construídos, com o intuito de validar de forma visual os resultados apresentados nas etapas 1 e 2. Indo desde correlações multivariadas, até mapas geográficos.
""", unsafe_allow_html=True)

st.markdown("""
```
AVISO: Devidos as restrições de 'Tamanho de Arquivos' no GitHub, 
abaixo foram usadas as amostras de 10% dos datasets!
```
""", unsafe_allow_html=True)

st.markdown("""
### Informações Básicas

Todos os datasets utilizados possuem o mesmo tipo de dados para suas respectivas colunas:

1. object para 'Dia', 'Estado', 'Municipio' e 'geometry'; 
2. float64 para 'DiaSemChuva', 'Precipitacao', 'RiscoFogo', 'Latitude', 'Longitude' e 'FRP'. 

A única diferença é o 'RangeIndex' na segunda linha das imagens. 
As duas imagens abaixo são apresentações resumidas de características gerais e numéricas dos datasets do INPE:
""", unsafe_allow_html=True)

st.image("./src/assets/statisticDescritive/image01.png")

st.markdown("""
O método *describe()* fornece uma visão ampla de alguns valores estatísticos, nos quais, há os valores mínimos e máximos, o desvio padrão, média e os quartis (25%, 50% e 75%) de cada classe. 
No caso dos datasets em questão, apenas as informações de 'DiaSemChuva', 'Precipitacao' e 'FRP'.
""", unsafe_allow_html=True)

###
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path1 = r"./db/inpe-2020/sample.csv"
dataset1 = pd.read_csv(path1, sep=",")
dataset1 = dataset1.drop(dataset1.columns[[0]], axis=1)

path2 = r"./db/inpe-2021/sample.csv"
dataset2 = pd.read_csv(path2, sep=",")
dataset2 = dataset2.drop(dataset2.columns[[0]], axis=1)

path3 = r"./db/inpe-2022/sample.csv"
dataset3 = pd.read_csv(path3, sep=",")
dataset3 = dataset3.drop(dataset3.columns[[0]], axis=1)

path4 = r"./db/inpe-2023/sample.csv"
dataset4 = pd.read_csv(path4, sep=",")
dataset4 = dataset4.drop(dataset4.columns[[0]], axis=1)
###

st.code("""
# aplicado nos demais datasets

dataset1.describe()
""", language="python")
st.write(dataset1.describe())

st.title("Visualização de Dados com Matplotlib")

st.code("""
# Plotar valores unicos

sns.countplot(dataset1['Estado'])
""", language="python")

plot = sns.countplot(dataset1['Estado'])
st.pyplot(plot.get_figure())

st.markdown("### Além disso, foram explorados as principais cidades com mais registros de queimada de cada estado")

st.code("""
# Classificando Histograma com Municipios

counts = pop_amaz['Municipio'].value_counts()

# Get the top 10 municipalities with the most temperature records
top_10 = counts.nlargest(10)

# Plot a histogram
plt.figure(figsize=(12,8))
plt.barh(top_10.index, top_10.values)
plt.xlabel('Numeros de focos localizados por Cidade')
plt.ylabel('Municipios')
plt.title('10 Municipios do Amazonas com mais registros em 4 anos')

plt.gca().invert_yaxis()  # Invert y-axis to have the municipality with the most records at the top
plt.show() # it works perfectly
""", language="python")

###
# Unindo os 4 datasets em 1
frames = [dataset1, dataset2, dataset3, dataset4]
dfMerged= pd.concat(frames)

pop_amaz = dfMerged[dfMerged['Estado'] == 'AMAZONAS']
counts = pop_amaz['Municipio'].value_counts()
top_10 = counts.nlargest(10)

fig = plt.figure(figsize=(12,8))
plt.barh(top_10.index, top_10.values)
plt.xlabel('Numeros de focos localizados por Cidade')
plt.ylabel('Municipios')
plt.title('10 Municipios do Amazonas com mais registros em 4 anos')
plt.gca().invert_yaxis()
plt.show()
###

st.pyplot(fig)

st.markdown("""
E por fim, foram feitos os *Heatmaps* (mapas de calor), porém, devido a baixíssima correlação das variáveis, 
os gráficos ficaram completamente idênticos em aparência, por isso, apenas um dos gráficos está disposto.
""", unsafe_allow_html=True)

st.code("""
# Correlação em Mapa de Calor

dataset_corr1 = dataset1.drop(dataset1.columns[[0, 1, 2, 6, 7]], axis=1)
sns.heatmap(dataset_corr1.corr()) # é o mesmo gráfico em todos os datasets
""", language="python")

###
dataset_corr1 = dataset1.drop(dataset1.columns[[0, 1, 2, 6, 7]], axis=1)
plot = sns.heatmap(dataset_corr1.corr())
###

st.pyplot(plot.get_figure())
