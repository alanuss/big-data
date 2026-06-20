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
# Generar CSV

np.random.seed(42)

output_dir = Path(__file__).parent
csv_path = output_dir / "ventas.csv"

ciudades = ["Santiago", "Valparaíso", "Concepción", "Puerto Montt"]
productos = ["Laptop", "Smartphone", "Tablet", "Accesorio"]
metodos_pago = ["Tarjeta", "Transferencia", "Efectivo"]
fechas = pd.date_range("2022-01-01", "2024-12-31")

df = pd.DataFrame(
    {
        "ID": np.arange(1, 1001),
        "Edad": np.random.randint(18, 66, size=1000),
        "Ciudad": np.random.choice(ciudades, size=1000),
        "Producto": np.random.choice(productos, size=1000),
        "Precio": np.random.randint(50, 2001, size=1000),
        "Cantidad": np.random.randint(1, 6, size=1000),
        "FechaCompra": np.random.choice(fechas, size=1000),
        "MétodoPago": np.random.choice(metodos_pago, size=1000),
    }
)

df.to_csv(csv_path, index=False)
print("Archivo generado en:", csv_path)

# %%
# 1. Exploración inicial

df = pd.read_csv(csv_path)

print("Primeras 10 filas:")
print(df.head(10))

registros_por_ciudad = df["Ciudad"].value_counts()
print("Registros por ciudad:")
print(registros_por_ciudad)

# %%
# 2. Estadísticas descriptivas

promedio_precios_producto = df.groupby("Producto")["Precio"].mean()
desviacion_edades = df["Edad"].std()
producto_mas_vendido = df.groupby("Producto")["Cantidad"].sum().idxmax()

print("Promedio de precios por producto:")
print(promedio_precios_producto)
print("Desviación estándar de edades:", desviacion_edades)
print("Producto más vendido en cantidad:", producto_mas_vendido)

# %%
# 3. Visualización

plt.figure(figsize=(8, 5))
plt.hist(df["Precio"], bins=20, color="skyblue", edgecolor="black")
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.title("Histograma de precios")
plt.savefig(output_dir / "histograma_precios.png")
plt.close()

ventas_por_ciudad = df.groupby("Ciudad")["Cantidad"].sum()

plt.figure(figsize=(8, 5))
ventas_por_ciudad.plot(kind="bar", color="orange")
plt.xlabel("Ciudad")
plt.ylabel("Cantidad vendida")
plt.title("Ventas por ciudad")
plt.tight_layout()
plt.savefig(output_dir / "ventas_por_ciudad.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["Precio"], df["Cantidad"], alpha=0.5)
plt.xlabel("Precio")
plt.ylabel("Cantidad")
plt.title("Relación entre precio y cantidad")
plt.savefig(output_dir / "precio_cantidad.png")
plt.close()

print("Gráficos guardados en la carpeta de la actividad")

# %%
# 4. Uso de NumPy

precios = df["Precio"].to_numpy()
precios_normalizados = (precios - precios.min()) / (precios.max() - precios.min())
percentiles = np.percentile(precios, [25, 50, 75])

print("Array de precios:")
print(precios)
print("Precios normalizados:")
print(precios_normalizados)
print("Percentiles 25, 50 y 75:")
print(percentiles)

# %%
# 5. Apriori

df["Transaccion"] = (df["ID"] - 1) // 4
transacciones = pd.get_dummies(df[["Transaccion", "Producto"]], columns=["Producto"])
matriz_transacciones = transacciones.groupby("Transaccion").max()
matriz_transacciones.columns = matriz_transacciones.columns.str.replace("Producto_", "")

frequent_itemsets = apriori(matriz_transacciones, min_support=0.05, use_colnames=True)
reglas = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
reglas = reglas[reglas["support"] > 0.05]

print("Conjuntos frecuentes:")
print(frequent_itemsets)
print("Reglas de asociación:")
print(reglas[["antecedents", "consequents", "support", "confidence", "lift"]])

# %%
# 6. KMeans

x = df[["Edad", "Precio", "Cantidad"]]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(x_scaled)

df["Cluster"] = clusters

print("Número de clientes por cluster:")
print(df["Cluster"].value_counts())

centroids = scaler.inverse_transform(kmeans.cluster_centers_)
for i, c in enumerate(centroids):
    print(
        f"Cluster {i}: Edad promedio = {c[0]:.2f}, Precio promedio = {c[1]:.2f}, Cantidad promedio = {c[2]:.2f}"
    )

plt.figure(figsize=(8, 5))
plt.scatter(df["Edad"], df["Precio"], c=df["Cluster"], cmap="viridis", alpha=0.6)
plt.xlabel("Edad")
plt.ylabel("Precio")
plt.title("Clusters de clientes")
plt.savefig(output_dir / "clusters_clientes.png")
plt.close()

print(
    "Los clusters separan clientes según edad, nivel de precio comprado y cantidad de productos adquiridos"
)
