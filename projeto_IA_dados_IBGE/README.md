# 🧠 Agrupamento de Estados Brasileiros com K-Means

Este projeto utiliza o algoritmo de aprendizado de máquina **K-Means** para agrupar os estados do Brasil com base em indicadores socioeconômicos, como IDH, renda per capita, educação, veículos, receitas e despesas públicas.

---

## 🎯 Objetivo

Aplicar a técnica de clusterização para identificar padrões entre os estados brasileiros a partir de dados fornecidos pelo IBGE e outras fontes públicas.

---

## 📁 Dados Utilizados

O dataset utilizado foi `ibge_estados1.csv`, contendo informações dos 26 estados e do Distrito Federal. As colunas utilizadas no modelo foram:

- `populacao`  
- `area`  
- `idh`  
- `renda_per_capita`  
- `total_veiculos`  
- `matricula_ensino_fundamental`  
- `total_desp_bru_empenhadas`  
- `total_rec_b_realizada`  

---

## ⚙️ Processamento dos Dados

1. **Carregamento dos dados** com `pandas`.
2. **Seleção das colunas relevantes**.
3. **Normalização** com `StandardScaler`.
4. **Aplicação do algoritmo K-Means** com diferentes valores de `k` para definir o número ideal de clusters com o **método do cotovelo**.
5. **Criação da coluna `cluster`** com a classificação de cada estado.
6. **Visualização gráfica** com `seaborn` e `matplotlib`.

---

## 📉 Método do Cotovelo

Foi utilizado o WCSS (*Within-Cluster Sum of Squares*) para determinar o número ideal de clusters. O gráfico sugeriu que **3 clusters** seria uma escolha apropriada.

---

## 📊 Visualizações

- Gráfico de dispersão com **IDH** e **renda per capita**, colorido por cluster.
- Inclusão das **siglas dos estados** diretamente no gráfico.
- Exibição de uma tabela com **sigla, governador e cluster** de cada estado.

---

## 🛠 Tecnologias Usadas

- Python 3
- pandas
- scikit-learn
- matplotlib
- seaborn

---

## 📌 Conclusão

A aplicação do K-Means possibilitou identificar padrões de desenvolvimento entre os estados. A partir dos clusters formados, é possível observar semelhanças regionais e subsidiar análises voltadas para políticas públicas e planejamento estratégico.

---

## 💡 Melhorias Futuras

- Aplicar **PCA** para reduzir dimensionalidade e melhorar a visualização.
- Testar outros métodos de agrupamento (como DBSCAN ou Hierárquico).
- Adicionar novos indicadores (ex: saúde, criminalidade, saneamento básico).

---

## 📎 Arquivo de Dados

Certifique-se de que o arquivo `ibge_estados1.csv` esteja presente na pasta do projeto para o correto funcionamento.

---

## 👤 Autora

- **Ladiane Santana** – estudante de Análise e Desenvolvimento de Sistemas
