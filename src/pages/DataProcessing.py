import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

st.markdown("""
A seção de “Tratamento dos Dados” é fortemente vinculada ao processo "E.T.L." (*Extract, Transform, Load*), ou seja, uma fase predecessora a análise e exploração dos dados obtidos. 

Nessa etapa, o dataset é minuciosamente trabalhado, e dependendo das informações a serem obtidas, o pesquisador deverá produzir novos dados, editar os dados existentes, e/ou remover os dados que possam ocasionar erros e incongruências nas próximas fases da pesquisa.

`Os cometários na parte superior de cada trecho de código são auto-explicativos. E foram aplicados em todos os datasets (2020, 2021, 2022 e 2023)`
""")

st.title("*Extract* - Extrair dados da Nuvem")

st.code("""
# extraindo dados do Google Drive
path1 = "/content/drive/MyDrive/TCC/dados-inpe-2020/dataset.csv"

dataset1 = pd.read_csv(path1, sep=",")
""", language="python")

st.title("*Transform* - Transformar")

st.code("""
# removendo colunas desnecessárias: 'Satelite', 'Pais', 'Bioma'

dataset1 = dataset1.drop(dataset1.columns[[1, 2, 5]], axis=1)
""", language="python")

st.code("""
# selecionar dados onde há possibilidade de incêndio: HFR >= 1

dataset1 = dataset1[dataset1['RiscoFogo'] >= 1]
""", language="python")

st.code("""
# substituir valores nulos

dataset1.replace(np.nan, '0', inplace = True)
""", language="python")

st.code("""
# converter as colunas em formato 'float64'

dataset1['DiaSemChuva'] = dataset1['DiaSemChuva'].astype(float)
dataset1['Precipitacao'] = dataset1['Precipitacao'].astype(float)
""", language="python")

st.code("""
# crie coluna 'geometry' com 'lat' e 'lon'

geopoint = [Point(xy) for xy in zip(dataset1['Longitude'], dataset1['Latitude'])]
gdf1 = gpd.GeoDataFrame(dataset1, crs='EPSG:4326', geometry=geopoint)
gdf1 = gdf1.to_crs(crs='EPSG:3857')
""", language="python")

st.code("""
# converte coluna 'Dia' de 'object' para 'datetime'

gdf1['Dia'] = pd.to_datetime(
    gdf1['Dia'],
    format='%Y/%m/%d',
    dayfirst=False
)
""", language="python")

st.code("""
gdf4.dtypes
""", language="python")

with st.expander("Tabela dos tipos de dados"):
  st.markdown("""
  | Coluna | Tipo |
  |-----|----------------|
  | Dia | datetime64[ns] |
  | Estado | object |
  | Municipio | object |
  | DiaSemChuva | float64 |
  | Precipitacao | float64 |
  | RiscoFogo | float64 |
  | Latitude | float64 |
  | Longitude | float64 |
  | FRP | object |
  | geometry | geometry |
  | dtype | object |
  """)

st.title("*Load* - Carregar para Nuvem")

st.code("""
# salvando dados no formato .csv

gdf1.to_csv(r"/content/drive/MyDrive/TCC/dados-inpe-2020/data_gdf.csv")
""", language="python")