# %%
# Importar las librerías necesarias (EJERCICIO 1)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# %%
# Generar datos de ejemplo y guardarlos en un archivo CSV (EJERCICIO 1)
n = 1000
np.random.seed(57)

datos = {
    "ID": range(1, n + 1),
    "Edad": np.random.randint(18, 81, n),
    "Ciudad": np.random.choice(
        ["Puerto Varas", "Puerto Montt", "Llanquihue", "Concepción", "Temuco"], n
    ),
    "HorasEjercicio": np.round(np.random.uniform(0, 10, n), 1),
    "IMC": np.round(np.random.uniform(15, 40, n), 1),
    "Fuma": np.random.choice(["Sí", "No"], n),
    "Consumo": np.random.choice(["Pescado", "Verduras", "Frutas"], n),
    "Consume_Fruta": np.random.choice([0, 1], n, p=[0.35, 0.65]),
    "Consume_Verdura": np.random.choice([0, 1], n, p=[0.30, 0.70]),
}

df = pd.DataFrame(datos)
df.to_csv("datos_salud.csv", index=False, encoding="utf-8")

# %%
# Manipulación de datos con Pandas (EJERCICIO 2)
df = pd.read_csv("datos_salud.csv")
print(df.head(n=10))

pacientes = df[(df["IMC"] > 30) & (df["HorasEjercicio"] < 2)]
print(pacientes)

promedio_imc_por_ciudad = df.groupby("Ciudad")["IMC"].mean()
print(promedio_imc_por_ciudad)

# %%
# Operaciones con NumPy (EJERCICIO 3)
horas_ejercicio = df["HorasEjercicio"].to_numpy()
percentil_90 = np.percentile(horas_ejercicio, 90)
print("90º percentil de horas de ejercicio:", percentil_90)

minmax_scaler = MinMaxScaler()
datos_normalizados = minmax_scaler.fit_transform(df[["HorasEjercicio"]])

# %%
# Gráficos (EJERCICIO 4)

# histograma de edades
plt.hist(df["Edad"])
plt.title("Distribución de Edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

# %%
# gráfico de dispersión entre IMC y horas de ejercicio
plt.scatter(x=df["IMC"], y=df["HorasEjercicio"])
plt.title("IMC vs Horas de Ejercicio")
plt.xlabel("IMC")
plt.ylabel("Horas de Ejercicio")
plt.show()

# %%
# Algoritmo apriori (EJERCICIO 5)

datos_binarios = df[["Consume_Fruta", "Consume_Verdura"]].astype(bool)
itemsets = apriori(datos_binarios, min_support=0.1, use_colnames=True)
reglas = association_rules(itemsets, metric="confidence", min_threshold=0.5)
reglas.to_csv("reglas_asociacion.csv", index=False, encoding="utf-8")
print(reglas)

# %%
# Clustering con K-means (EJERCICIO 6)

## 1. Calcular los clusters

x = df[["Edad", "IMC", "HorasEjercicio"]]

scaler = StandardScaler()
x_escalado = scaler.fit_transform(x)

kmeans = KMeans(n_clusters=3, random_state=57)
clusters = kmeans.fit_predict(x_escalado)

df["Cluster"] = clusters
print("Número de personas por cluster:")
print(df["Cluster"].value_counts())

## 2. Interpretar los clusters usando promedios
promedios_cluster = df.groupby("Cluster")[["Edad", "IMC", "HorasEjercicio"]].mean()
print("Promedios por cluster:")
print(promedios_cluster)

for cluster, valores in promedios_cluster.iterrows():
    print(
        f"Cluster {cluster}: edad promedio {valores['Edad']:.2f}, "
        f"IMC promedio {valores['IMC']:.2f}, "
        f"horas de ejercicio promedio {valores['HorasEjercicio']:.2f}."
    )

centroids = scaler.inverse_transform(kmeans.cluster_centers_)

# %%
# Gráfico de los clusters

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

scatter = ax.scatter(
    df["Edad"],
    df["IMC"],
    df["HorasEjercicio"],
    c=df["Cluster"],
    cmap="viridis",
    alpha=0.7,
)

ax.scatter(
    centroids[:, 0],
    centroids[:, 1],
    centroids[:, 2],
    c="red",
    marker="X",
    s=200,
    label="Centroides",
)

ax.set_title("Clusters K-means en 3D")
ax.set_xlabel("Edad")
ax.set_ylabel("IMC")
ax.set_zlabel("Horas de Ejercicio")
fig.colorbar(scatter, ax=ax, label="Cluster")
ax.legend()

plt.show()
