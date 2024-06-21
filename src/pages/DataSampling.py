import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

st.markdown("""
Uma amostragem estatística é uma distribuição probabilística, baseada na retirada de amostras, com um alto grau de aleatoriedade, e um tamanho fixo, na população pesquisada. 
Distribuições probabilísticas ajudam o pesquisador a entender como os resultados de amostra variam entre as amostras. 
Os métodos de amostragem são técnicas utilizadas para selecionar um subconjunto de unidades da população com o objetivo de realizar análises estatísticas ou pesquisas. 
([*FROST, Jim*](https://statisticsbyjim.com/hypothesis-testing/sampling-distribution/); [*HASSAN, Muhammad*](https://www.google.com/url?q=https://researchmethod.net/sampling-methods/&sa=D&source=docs&ust=1718890332471500&usg=AOvVaw3ln8LDCgAN8AYPLR1EEuHZ)).

---

E entre os tipos de amostragem estatística dispostos, foram escolhidas:

1. Amostragem aleatória simples (Amostragem Probabilística) - Todos os membros da população têm chances iguais de serem selecionados para a amostra.
2. Amostragem proposital (Amostragem não probabilística) - Os participantes são selecionados com base em critérios específicos, como experiência ou conhecimento sobre um determinado tema.

---

Os métodos de amostragem devem ser conduzidos em 6 etapas:

1. Definição da população: os 4 datasets do INPE
2. Escolha dos métodos de amostragem: Amostragem aleatória simples e Amostragem proposital são 2 métodos simples e aplicáveis. 
3. Determinar o tamanho das amostras: Cada amostra utiliza 10% da população em cada dataset. Com uma modificação: os dados da classe ‘DiaSemChuva’ foram manipulados para exibir os dados no intervalo 0 - 120.
4. Selecionar amostra: As amostras devem ser selecionadas aleatoriamente e/ou, quando utilizado um método não aleatório, todos os esforços devem ser feitos para minimizar o viés e garantir que a amostra seja representativa.
5. Coleta de dados: os dados foram coletados anteriormente no BDQueimadas do INPE.
6. Analisar os dados: etapa essa que vem logo a seguir, onde os dados serão transformados em informação.
""", unsafe_allow_html=True)

st.title("Distribuição Probabilística")

st.code("""
sample_proportion = 0.01
sample_size = int(pop_dataset_size * sample_proportion)
simple_random_sample = np.random.choice(dataset['DiaSemChuva'], sample_size)

x = simple_random_sample
hist_data = [x]
group_labels = ['DiaSemChuva'] # name of the dataset label

fig = ff.create_distplot(
  hist_data,
  group_labels
)

fig.show()
""", language="python")

with st.expander("Veja os resultados"):
    st.image(
        "./src/assets/dataSampling/distribution-prob/sample01.png", 
        caption="Amostra da População de 2020"
    )
    st.image(
        "./src/assets/dataSampling/distribution-prob/sample02.png", 
        caption="Amostra da População de 2021"
    )
    st.image(
        "./src/assets/dataSampling/distribution-prob/sample03.png", 
        caption="Amostra da População de 2022"
    )
    st.image(
        "./src/assets/dataSampling/distribution-prob/sample04.png", 
        caption="Amostra da População de 2023"
    )

st.title("Distribuição Não Probabilística")

st.code("""
sample = dataset.sample(frac=0.1, replace=True, random_state=1)

pop_sample_size = len(sample)
sample_proportion = 0.1

sample_size = int(pop_sample_size * sample_proportion)
simple_random_sample = np.random.choice(sample['DiaSemChuva'], sample_size)

x = simple_random_sample
hist_data = [x]
group_labels = ['DiaSemChuva']

fig = ff.create_distplot(
  hist_data,
  group_labels
)

fig.show()
""", language="python")

with st.expander("Veja os resultados"):
    st.image(
        "./src/assets/dataSampling/distribution-non-prob/sample01.png", 
        caption="Amostra da População de 2020"
    )
    st.image(
        "./src/assets/dataSampling/distribution-non-prob/sample02.png", 
        caption="Amostra da População de 2021"
    )
    st.image(
        "./src/assets/dataSampling/distribution-non-prob/sample03.png", 
        caption="Amostra da População de 2022"
    )
    st.image(
        "./src/assets/dataSampling/distribution-non-prob/sample04.png", 
        caption="Amostra da População de 2023"
    )
