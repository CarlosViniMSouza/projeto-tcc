import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

st.markdown("""
A arquitetura elaborada é dividida em 3 ambientes:

1. **Google Drive:** Aplicação da Google para armazenamento de arquivos - no caso, guardamos os datasets e notebooks.
2. **Google Collab:** Ambiente de Desenvolvimento da Google para produção do código para atender as demandas do projeto.
3. **Streamlit:** Biblioteca Python para dispor modelos de *ML* e estudos de Análise de Dados na web.
""", unsafe_allow_html=True)

st.image("./src/static/architecture-project.png")
