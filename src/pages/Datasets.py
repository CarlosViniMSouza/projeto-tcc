import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

st.markdown("""
O INPE fornece conjuntos de dados anuais em diversos formatos (.csv; .GeoJson; .kml; .shapefile) com acesso ao público em geral ([BDQueimadas](https://terrabrasilis.dpi.inpe.br/queimadas/bdqueimadas/)).
O INMET disponibiliza os datasets de duas formas temporais: anualmente e semestralmente (essa pesquisa trabalha com dados coletados anualmente).
Porém, diferentemente do INPE, há apenas o fornecimento em arquivos .csv (o que limita as possibilidades a serem exploradas mais á frente).
""", unsafe_allow_html=True)

st.title("Página do BDQueimadas & Forms")
st.image("./src/static/pag-bdqueimadas.png")
st.image("./src/static/forms-bdqueimadas.png")
