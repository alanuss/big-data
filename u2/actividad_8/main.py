# %%
# Imports
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# %%
# Generación del CSV

np.random.seed(42)

output_dir = Path(__file__).parent
csv_path = output_dir / "estudiantes.csv"

carreras = ["Informática", "Ingeniería", "Medicina", "Derecho", "Arquitectura"]
ciudades = ["Santiago", "Valparaíso", "Concepción", "Puerto Montt"]

carrera = np.random.choice(carreras, size=1000)
probabilidad_beca = np.where(
    np.isin(carrera, ["Informática", "Medicina"]),
    0.6,
    0.35,
)
beca = np.where(np.random.random(size=1000) < probabilidad_beca, "Sí", "No")

df = pd.DataFrame(
    {
        "ID": np.arange(1, 1001),
        "Carrera": carrera,
        "Edad": np.random.randint(18, 31, size=1000),
        "PromedioNotas": np.round(np.random.uniform(3.5, 7.0, size=1000), 1),
        "HorasEstudioSemanal": np.random.randint(0, 41, size=1000),
        "Asistencia": np.round(np.random.uniform(50, 100, size=1000), 1),
        "Ciudad": np.random.choice(ciudades, size=1000),
        "Beca": beca,
    }
)

df.to_csv(csv_path, index=False)
print("Archivo generado en:", csv_path)

# %%
# 1. Exploración inicial

df = pd.read_csv(csv_path)

print("Primeras filas:")
print(df.head())

estudiantes_por_carrera = df["Carrera"].value_counts()
print("Estudiantes por carrera:")
print(estudiantes_por_carrera)

# %%
# 2. Estadísticas descriptivas

promedio_notas_carrera = df.groupby("Carrera")["PromedioNotas"].mean()
media_horas_estudio = df["HorasEstudioSemanal"].mean()
porcentaje_beca = (df["Beca"] == "Sí").mean() * 100
alumnos_por_ciudad = df["Ciudad"].value_counts()

print("Promedio de notas por carrera:")
print(promedio_notas_carrera)
print("Media de horas de estudio semanal:", media_horas_estudio)
print("Porcentaje de estudiantes con beca:", porcentaje_beca)
print("Cantidad de alumnos por ciudad:")
print(alumnos_por_ciudad)

# %%
# 3. Visualización

plt.figure(figsize=(8, 5))
plt.hist(df["HorasEstudioSemanal"], bins=20, color="skyblue", edgecolor="black")
plt.xlabel("Horas de estudio semanal")
plt.ylabel("Frecuencia")
plt.title("Histograma de horas de estudio")
plt.savefig(output_dir / "histograma_horas_estudio.png")
plt.close()

promedio_notas_ciudad = df.groupby("Ciudad")["PromedioNotas"].mean()

plt.figure(figsize=(8, 5))
promedio_notas_ciudad.plot(kind="bar", color="orange")
plt.xlabel("Ciudad")
plt.ylabel("Promedio de notas")
plt.title("Promedio de notas por ciudad")
plt.tight_layout()
plt.savefig(output_dir / "promedio_notas_ciudad.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["HorasEstudioSemanal"], df["PromedioNotas"], alpha=0.5)
plt.xlabel("Horas de estudio semanal")
plt.ylabel("Promedio de notas")
plt.title("Horas de estudio vs promedio de notas")
plt.savefig(output_dir / "horas_promedio_notas.png")
plt.close()

print("Gráficos guardados en la carpeta de la actividad")

# %%
# 4. NumPy

asistencia = df["Asistencia"].to_numpy()
percentiles_asistencia = np.percentile(asistencia, [25, 50, 75])

horas_estudio = df["HorasEstudioSemanal"].to_numpy()
horas_estudio_normalizadas = (horas_estudio - horas_estudio.min()) / (
    horas_estudio.max() - horas_estudio.min()
)

print("Percentiles de asistencia 25, 50 y 75:")
print(percentiles_asistencia)
print("Horas de estudio normalizadas:")
print(horas_estudio_normalizadas)

# %%
# 5. Apriori

matriz_transacciones = pd.get_dummies(df[["Carrera", "Beca"]])

frequent_itemsets = apriori(matriz_transacciones, min_support=0.05, use_colnames=True)
reglas = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)

reglas_carrera_beca = reglas[
    reglas["antecedents"].astype(str).str.contains("Carrera")
    & reglas["consequents"].astype(str).str.contains("Beca")
]

print("Conjuntos frecuentes:")
print(frequent_itemsets)
print("Reglas de asociación entre carrera y beca:")
print(reglas_carrera_beca[["antecedents", "consequents", "support", "confidence", "lift"]])

# %%
# 6. KMeans

x = df[["Edad", "PromedioNotas", "HorasEstudioSemanal"]]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(x_scaled)

df["Cluster"] = clusters

print("Número de estudiantes por cluster:")
print(df["Cluster"].value_counts())

centroids = scaler.inverse_transform(kmeans.cluster_centers_)
for i, c in enumerate(centroids):
    print(
        f"Cluster {i}: Edad promedio = {c[0]:.2f}, Promedio notas = {c[1]:.2f}, Horas estudio = {c[2]:.2f}"
    )

plt.figure(figsize=(8, 5))
plt.scatter(
    df["HorasEstudioSemanal"],
    df["PromedioNotas"],
    c=df["Cluster"],
    cmap="viridis",
    alpha=0.6,
)
plt.xlabel("Horas de estudio semanal")
plt.ylabel("Promedio de notas")
plt.title("Clusters de estudiantes")
plt.savefig(output_dir / "clusters_estudiantes.png")
plt.close()

print(
    "Los clusters muestran perfiles según edad, rendimiento académico y cantidad de horas de estudio semanal"
)
