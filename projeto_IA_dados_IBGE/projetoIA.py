import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Carregue o CSV (ajuste o caminho se necessário)
df = pd.read_csv("ibge_estados1.csv")

# Visualize as primeiras linhas
print(df.head())

# Seleciona colunas relevantes para análise
colunas_para_cluster = ['populacao', 'area', 'idh', 'renda_per_capita',
                        'total_veiculos', 'matricula_ensino_fundamental',
                        'total_desp_bru_empenhadas', 'total_rec_b_realizada']

dados = df[colunas_para_cluster]

# Normaliza os dados para evitar distorções (muito importante!)
scaler = StandardScaler()
dados_normalizados = scaler.fit_transform(dados)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(dados_normalizados)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Método do Cotovelo')
plt.xlabel('Número de Clusters')
plt.ylabel('WCSS')
plt.show()

# Digamos que o cotovelo mostrou 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(dados_normalizados)

# Veja os grupos
print(df[['sigla', 'cluster']])

sns.scatterplot(data=df, x='renda_per_capita', y='idh', hue='cluster', palette='Set2')
plt.title('Estados agrupados por IDH e Renda per Capita')

# Colocar as siglas dos estados ao lado dos pontos
for i, row in df.iterrows():
    plt.text(row['renda_per_capita'], row['idh'], row['sigla'], fontsize=9,
             verticalalignment='bottom', horizontalalignment='right')

plt.show()

print(df[['sigla', 'governador', 'cluster']].sort_values('cluster'))
