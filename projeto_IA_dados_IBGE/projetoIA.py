import pandas as pd  # Biblioteca para manipulação de dados
from sklearn.cluster import KMeans  # Algoritmo de agrupamento
from sklearn.preprocessing import StandardScaler  # Para normalização dos dados
import matplotlib.pyplot as plt  # Para visualização de gráficos
import seaborn as sns  # Biblioteca de visualização mais estilizada


df = pd.read_csv("ibge_estados1.csv")  # Carrega o dataset com dados dos estados do Brasil
print(df.head())  # Mostra as 5 primeiras linhas do DataFrame


# Visualize as primeiras linhas
print(df.head())

# Seleciona colunas que serão usadas para o agrupamento
colunas_para_cluster = ['populacao', 'area', 'idh', 'renda_per_capita',
                        'total_veiculos', 'matricula_ensino_fundamental',
                        'total_desp_bru_empenhadas', 'total_rec_b_realizada']
dados = df[colunas_para_cluster]  # Cria novo DataFrame com essas colunas


scaler = StandardScaler()  # Cria o objeto para normalização
dados_normalizados = scaler.fit_transform(dados)  # Normaliza os dados para que fiquem na mesma escala


wcss = []  # Lista que armazenará os valores de WCSS (soma dos quadrados intra-cluster)
for i in range(1, 11):  # Testa de 1 a 10 clusters
    kmeans = KMeans(n_clusters=i, random_state=42)  # Inicializa o KMeans com i clusters
    kmeans.fit(dados_normalizados)  # Treina o modelo
    wcss.append(kmeans.inertia_)  # Salva a inércia (WCSS)

#  KMeans, um algoritmo de aprendizado de máquina não supervisionado (clusterização), para agrupar os dados.
# Todo o trecho que calcula e avalia os clusters com base na inércia (wcss) é o núcleo da IA nesse projeto.

# WCSS significa "Within-Cluster Sum of Squares", ou seja, Soma dos Quadrados Intra-cluster.

# Ele mede o quão próximos os pontos estão do centro (centróide) de seus respectivos clusters. 
# Quanto menor o WCSS, mais compactos e bem definidos são os clusters. Neste código, 
# ele é usado para ajudar a decidir a quantidade ideal de clusters com o método do cotovelo.

plt.plot(range(1, 11), wcss, marker='o')  # Plota gráfico do método do cotovelo
plt.title('Método do Cotovelo')  # Título do gráfico
plt.xlabel('Número de Clusters')  # Eixo X
plt.ylabel('WCSS')  # Eixo Y
plt.show()  # Exibe o gráfico


kmeans = KMeans(n_clusters=3, random_state=42)  # Define 3 clusters com base no gráfico
df['cluster'] = kmeans.fit_predict(dados_normalizados)  # Aplica o modelo e adiciona a coluna 'cluster' ao DataFrame


print(df[['sigla', 'cluster']])  # Exibe a sigla dos estados e a qual grupo (cluster) eles pertencem


# Plota gráfico com eixo x = renda per capita e eixo y = IDH, colorido por cluster
sns.scatterplot(data=df, x='renda_per_capita', y='idh', hue='cluster', palette='Set2')
plt.title('Estados agrupados por IDH e Renda per Capita')


# Adiciona o nome dos estados no gráfico, ao lado dos pontos
for i, row in df.iterrows():
    plt.text(row['renda_per_capita'], row['idh'], row['sigla'], fontsize=9,
             verticalalignment='bottom', horizontalalignment='right')

plt.show()  # Exibe o gráfico


# Exibe a sigla, nome do governador e cluster de cada estado, ordenado pelo número do cluster
print(df[['sigla', 'governador', 'cluster']].sort_values('cluster'))

