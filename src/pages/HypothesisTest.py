import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

st.markdown("""
Testes de hipótese são uma ramificação da estatística que avalia a precisão de teorias propostas, 
testando-as em relação aos dados. Permite ao pesquisador, avaliar a importância dos resultados e tomar decisões sobre aceitar ou rejeitar uma determinada hipótese. 
Os testes de hipóteses não são totalmente precisos, pois envolvem amostras aleatórias para obter conclusões a respeito da população. 
([BROWNLEE, Jason; 2021](https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/); [FROST, Jim](https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/)).
""")

st.markdown("""
Há 5 categorias de Testes de Hipótese Estatística que podem ser aproveitados, dentre os quais, temos:

1. **Testes de normalidade:** Checar se os dados têm uma distribuição gaussiana. No qual o teste optado foi o "*Teste de Shapiro-Wilk*", por sua simplicidade ao testar se uma amostra se encontra na distribuição gaussiana.
2. **Testes de Correlação:** Checar se duas amostras estão relacionadas. Um dos testes mais conhecidos da literatura atual é o "*Coeficiente de Correlação de Pearson*", que visa demonstrar a correlação linear entre as amostras.
3. **Testes Estacionários:** Checar se uma série temporal é estacionária ou não. Há 2 testes dessa categoria, e o "*Teste de raiz unitária Dickey-Fuller aumentado*" foi a escolha da pesquisa, pois verifica se uma série temporal tem uma raiz unitária, ou seja, se há uma tendência nos valores; mais conhecido como ‘autorregressivo’.
4. **Testes de hipóteses estatísticas paramétricas:** Nessa categoria, comparamos as amostras obtidas. E o "*Teste de Análise de Variância (ANOVA - Analysis of Variance Test)*" testa se as médias de duas ou mais amostras independentes são significativamente diferentes, além de ser um tipo de teste muito abordado em estudos estatísticos no geral.
5. **Testes de hipóteses estatísticas não paramétricas:** Usado como alternativa aos testes paramétricos, podendo ser empregados apenas se os dados subjacentes satisfizerem certos critérios e suposições. O "*Teste de Friedman*" verifica se as distribuições de várias amostras pareadas são semelhantes.

O resultados dos testes aplicados estão tabelados abaixo:
""")

st.markdown("""
| Tipos\Dataset | 2020 | 2021 | 2022 | 2023 |
|---------------|------|------|------|------|
| Teste de Shapiro-Wilk | Provavelmente Não Gaussiano | Provavelmente Não Gaussiano | Provavelmente Não Gaussiano | Provavelmente Não Gaussiano |
| Coeficiente de Correlação de Pearson | Provavelmente independente | Provavelmente independente | Provavelmente independente | Provavelmente independente |
| Teste de raiz unitária Dickey-Fuller aumentado | Provavelmente Estacionário | Provavelmente Estacionário | Provavelmente Estacionário | Provavelmente Estacionário |
| Teste de Análise de Variância (ANOVA) | Provavelmente a mesma distribuição | Provavelmente a mesma distribuição | Provavelmente a mesma distribuição | Provavelmente a mesma distribuição |
| Teste de Friedman | Provavelmente a mesma distribuição | Provavelmente a mesma distribuição | Provavelmente a mesma distribuição | Provavelmente a mesma distribuição |
""")
