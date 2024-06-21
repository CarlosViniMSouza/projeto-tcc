- **Artigo 24: Previsão de desempenho de aprendizado de máquina, séries temporais e métodos híbridos para séries temporais de baixa e alta frequência.**

```md
Um dos principais objetivos da análise de séries temporais é a previsão, por isso tanto métodos de aprendizado de máquina quanto métodos estatísticos têm sido propostos na literatura. Neste estudo, comparamos o desempenho de previsão de algumas dessas abordagens. Além dos métodos tradicionais de previsão, que são os Métodos Naive e Sazonal Naive, S/ARIMA, Suavização Exponencial, TBATS, Modelos de Suavização Exponencial Bayesiana com Modificações de Tendência e Decomposição STL, as previsões também são obtidas usando sete métodos diferentes de aprendizado de máquina, que são Random Forest, Support Vector Regression, XGBoosting, BNN, RNN, LSTM e FFNN, e a hibridização de séries temporais estatísticas e métodos de aprendizado de máquina.

O conjunto de dados é selecionado proporcionalmente a partir de vários domínios de tempo no conjunto de dados M4 Competition. Assim, pretendemos criar um guia de previsão considerando diferentes abordagens de pré-processamento, métodos e conjuntos de dados com vários domínios de tempo. Após o experimento, o desempenho e o impacto de todos os métodos são discutidos. Portanto, a maioria dos melhores modelos são selecionados principalmente a partir de métodos de aprendizado de máquina para previsão.

Além disso, o desempenho da previsão do modelo é afetado tanto pela frequência temporal quanto pelo horizonte de previsão. Por último, o estudo sugere que a abordagem híbrida nem sempre é o melhor modelo para previsão. Portanto, este estudo fornece diretrizes para entender qual método terá melhor desempenho em diferentes frequências de séries temporais.

*PALAVRAS-CHAVE: previsão, método híbrido, aprendizado de máquina, análise de séries temporais*
```

- **Artigo 25: Previsão da abundância de insetos usando incorporação de séries temporais e aprendizado de máquina.**

```
A implementação de sistemas de monitoramento de insetos oferece uma excelente oportunidade para criar intervenções precisas para o controle de insetos. No entanto, a seleção do momento apropriado para uma intervenção ainda é uma questão em aberto devido à dificuldade inerente à implementação do monitoramento in loco em tempo real. Esta decisão é ainda mais crítica com espécies de insetos que podem aumentar abruptamente o tamanho da população. Uma possível solução para melhorar a tomada de decisões é aplicar métodos de previsão para prever a abundância de insetos.

No entanto, outra camada de complexidade é adicionada quando outras covariáveis ​​são consideradas na previsão, tais como séries temporais climáticas recolhidas ao longo do sistema de monitorização. Múltiplas combinações possíveis de séries temporais climáticas e suas defasagens podem ser usadas para construir um método de previsão. Portanto, este artigo de pesquisa propõe uma nova abordagem para resolver esse problema, combinando estatística, aprendizado de máquina e incorporação de séries temporais:

1. Utilizamos dois conjuntos de dados contendo uma série temporal de pulgões e dados climáticos coletados semanalmente nos municípios de Coxilha e Passo Fundo, no Sul do Brasil, durante oito anos.

2. Realizamos um estudo de simulação baseado em um modelo probabilístico autorregressivo com séries temporais exógenas baseadas em Poisson e distribuições binomiais negativas para verificar a influência da incorporação de séries temporais climáticas no desempenho de nossa abordagem.

3. Pré-processamos os dados usando nossa abordagem recém-proposta e abordagens mais diretas comumente usadas para treinar algoritmos de aprendizado de máquina em problemas de séries temporais.

4. Avaliamos o desempenho dos algoritmos de máquina selecionados observando a raiz do erro quadrático médio obtido usando a previsão um passo à frente.

Com base em Random Forests, regressão linear regulada por Lasso e algoritmos de regressão LightGBM, nossa nova abordagem produz previsões competitivas enquanto seleciona automaticamente abundâncias de insetos, séries temporais climáticas e suas defasagens para auxiliar na previsão.
```

- **Artigo 26: Algoritmos de aprendizado de máquina para análise e previsão de séries temporais.**

```md
Os dados de séries temporais estão sendo usados ​​em todos os lugares, desde registros de vendas até métricas de evolução da saúde dos pacientes. A capacidade de lidar com esses dados tornou-se uma necessidade, e para isso são utilizadas análises e previsões de séries temporais. Todo entusiasta do aprendizado de máquina consideraria essas ferramentas muito importantes, pois aprofundam a compreensão das características dos dados.

A previsão é usada para prever o valor de uma variável no futuro, com base em suas ocorrências passadas. Um levantamento detalhado dos vários métodos usados ​​para previsão foi apresentado neste papel. O processo completo de previsão, desde o pré-processamento até a validação, também foi explicado detalhadamente. Vários modelos estatísticos e de aprendizagem profunda foram considerados, nomeadamente ARIMA, Prophet e LSTMs.

Versões híbridas de modelos de Machine Learning também foram exploradas e elucidadas. Nosso trabalho pode ser usado por qualquer pessoa para desenvolver uma boa compreensão do processo de previsão e para identificar vários modelos de última geração que estão sendo usados ​​atualmente.

*Termos de Indexação: Aprendizado de Máquina, Análise de Séries Temporais, Previsão de Séries Temporais, Backtesting.*
```

- **Artigo 27: Previsão de série temporal de tráfego da Web usando o modelo de aprendizado de máquina Prophet.**

```md
A previsão do tráfego da web é fundamental para que proprietários de sites, profissionais de marketing e organizações tomem decisões informadas, planejem o desenvolvimento futuro, gerenciem adequadamente os recursos e otimizem sua presença online. Lidar com o tráfego online era um procedimento mais simples e menos complicado nos primeiros dias da Internet e do desenvolvimento web em comparação com os padrões atuais.

A internet ainda estava em seus estágios iniciais e os sites eram mais simples. Nos últimos anos, lidar com o tráfego online com modelos de série temporal de aprendizado de máquina (ML) tornou-se mais complexo. Algoritmos de aprendizado de máquina podem fornecer projeções precisas e insights úteis sobre tendências de tráfego online. Usando o Facebook Prophet, um popular kit de ferramentas de previsão, este modelo explica o processo de previsão de séries temporais e a avaliação de desempenho para dados de tráfego online.

A capacidade do Prophet de lidar com dados complicados de séries temporais com muitos componentes sazonais e feriados ganhou seu apelo. Os modelos de média móvel (MA) foram usados ​​para previsão no tempo, mas há certos limites e desvantagens no uso de dados de séries temporais para capturar e prever tendências subjacentes. O MA foi projetado especificamente para previsões de curto prazo, capturando dependências de curto prazo e flutuações aleatórias.

No entanto, o modelo Profeta foi projetado para lidar com dados de séries temporais com vários padrões sazonais, como sazonalidade diária, semanal e anual. Fornecemos uma explicação detalhada do modelo de série temporal do Profeta e avaliação para dados de tráfego da web usando o Facebook Prophet, com foco na compreensão do desempenho e visualização do modelo.

*Palavras-chave: Média Móvel; Profeta da Previsão; Séries Temporais; Tráfego Web; Sazonalidade do Facebook; Tendências de tráfego on-line; kit de ferramentas de previsão; Lidando com o tráfego online.*
```

- **Artigo 28: Algoritmo de aprendizado de máquina automatizado usando rede neural recorrente para realizar previsões de séries temporais de longo prazo.**

```md
A previsão de séries temporais de longo prazo permanece como um domínio de pesquisa crucial no domínio do aprendizado de máquina automatizado (AutoML). Atualmente, a previsão, seja ela baseada no aprendizado de máquina ou no aprendizado estatístico, normalmente depende da contribuição de especialistas e exige um envolvimento manual substancial. Esse esforço manual abrange o desenvolvimento de modelos, engenharia de recursos, ajuste de hiperparâmetros e a construção complexa de modelos de séries temporais. A complexidade destas tarefas torna a automação completa inviável, uma vez que exigem inerentemente a intervenção humana em múltiplas conjunturas.

Para superar esses desafios, este artigo propõe aproveitar a memória longa e de curto prazo, que é a variante das redes neurais recorrentes, aproveitando células de memória e mecanismos de controle para facilitar a previsão de séries temporais de longo prazo. No entanto, a precisão da previsão por redes neurais específicas e modelos tradicionais pode ser significativamente degradada ao abordar tarefas de séries temporais de longo prazo. Portanto, nossa pesquisa demonstra que esta abordagem inovadora supera o método tradicional de média móvel integrada autoregressiva (ARIMA) na previsão de séries temporais univariadas de longo prazo.

ARIMA é um modelo competitivo e de alta qualidade na previsão de séries temporais, mas requer esforços significativos de pré-processamento. Usando múltiplas métricas de precisão, avaliamos tanto o ARIMA quanto o método proposto nos dados simulados de séries temporais e dados reais em curto e longo prazo. Além disso, nossas descobertas indicam sua superioridade sobre arquiteturas de rede alternativas, incluindo redes neurais totalmente conectadas, redes neurais convolucionais e redes neurais convolucionais sem pooling. Nossa abordagem AutoML permite que não profissionais obtenham previsões de séries temporais altamente precisas e eficazes e pode ser amplamente aplicada a vários domínios, especialmente em negócios e finanças.

*PALAVRAS-CHAVE: Aprendizado de máquina automatizado; média móvel integrada autoregressiva; redes neurais; análise de série temporal.*
```

- **Artigo 29: Uma análise comparativa de técnicas avançadas de aprendizado de máquina para previsão de séries temporais de fluxo de rios.**

```md
Este estudo examina a contribuição dos dados de precipitação (RF) na melhoria da precisão da previsão de vazões de modelos avançados de aprendizado de máquina (ML) na Bacia do Rio Syr Darya. Diferentes conjuntos de cenários incluíram dados de precipitação de diferentes estações meteorológicas localizadas em diversas localizações geográficas em relação à estação de monitorização de caudal.

Modelos baseados em memória de longo e curto prazo (LSTM) foram usados ​​para examinar a contribuição dos dados de precipitação no desempenho da previsão de vazão, investigando cinco cenários em que dados de RF de diferentes estações meteorológicas foram incorporados dependendo de suas posições geográficas.

Especificamente, o cenário All-RF incluiu todos os dados de precipitação recolhidos em 11 estações; Upstream-RF (Up-RF) e Downstream-RF (Down-RF) incluíram apenas os dados de precipitação medidos a montante e a jusante da estação de medição de vazão; Pearson-RF (P-RF) incluiu apenas os dados de precipitação exibindo o mais alto nível de correlação com os dados de vazão, e o cenário Somente Fluxo (FO) incluiu dados de vazão.

As métricas de avaliação utilizadas para avaliar quantitativamente o desempenho dos modelos incluíram o RMSE, MAE e o coeficiente de determinação, R2. Ambos os modelos ML tiveram melhor desempenho no cenário FO, o que mostra que a diversidade de características de entrada (dados hidrológicos e meteorológicos) não melhorou a precisão preditiva, independentemente das posições das estações meteorológicas.

Os resultados mostram que os cenários P-RF produziram melhor precisão de previsão em comparação com todos os outros cenários, incluindo dados de precipitação, o que sugere que apenas os dados de precipitação a montante da estação de monitorização de caudal tendem a contribuir positivamente para o desempenho de previsão do modelo.

As descobertas evidenciam a adequação de redes simples baseadas em LSTM monocamada com apenas dados de vazão como recursos de entrada para aplicações de previsão de vazão fluvial de alto desempenho e econômicas, minimizando o tempo de processamento de dados.

*Palavras-chave: previsão de vazão fluvial; gestão de recursos hídricos; inteligência artificial; aprendizado de máquina; Redes LSTM; Ásia Central*
```

- **Artigo 30: Um pipeline de aprendizado de máquina para previsão de séries temporais no setor bancário.**

```md
O problema da previsão de séries temporais é amplamente debatido. Nos últimos anos, os algoritmos de aprendizado de máquina têm sido muito prolíficos nesta área. Este artigo descreve uma abordagem sistemática para construir um modelo preditivo de aprendizado de máquina para resolver problemas de otimização no setor bancário. É apresentada uma análise da literatura sobre a aplicação de tais métodos nesta área específica.

Como resultado direto da pesquisa descrita, foi desenvolvido um cenário universal para previsão de diversas séries temporais não estacionárias em modo automático. É considerado o cenário desenvolvido para a resolução de tarefas bancárias específicas para melhorar a eficiência do negócio, incluindo a otimização da procura de ATMs, previsão de carga no call center e cash center. É descrita uma metodologia de aprendizado de máquina em economia que pode produzir resultados robustos e reprodutíveis e pode ser reutilizada na resolução de outras tarefas semelhantes.

A metodologia descrita no artigo foi testada em três casos e mostrou a capacidade de gerar modelos com precisão superior a modelos preditivos semelhantes descritos na literatura por pelo menos pelo menos três pontos percentuais. Este artigo será útil para especialistas que lidam com o problema de previsão de séries temporais econômicas e para estudantes e pesquisadores devido ao grande número de links para revisões sistemáticas da literatura sobre este tema.

*Palavras-chave: aprendizado de máquina; redes neurais artificiais; mineração de dados; Caixas eletrônicos; previsão de séries temporais; previsão de carga; otimização de serviço*
```
