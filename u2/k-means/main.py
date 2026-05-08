# %%
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# %%
df = pd.read_csv("clientes.csv")
df.head()
# df.info()

# %%
x = df[["Edad", "Gasto_Mensual"]]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# %%
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(x_scaled)

# %%
df["Cluster"] = clusters
print("Número de clientes por cluster:")
print(df["Cluster"].value_counts())

# %%
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
# print(centroids)
for i, c in enumerate(centroids):
    print(
        f"Cluster {i}: Edad promedio = {c[0]:.2f}, Gasto mensual promedio = {c[1]:.2f}"
    )

# %%
plt.figure(figsize=(10, 6))
plt.scatter(df["Edad"], df["Gasto_Mensual"], c=df["Cluster"], cmap="viridis", alpha=0.6)
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c="red",
    marker="X",
    s=200,
    label="Centroides",
)
plt.xlabel("Edad")
plt.ylabel("Gasto Mensual")
plt.title("Segmentación de Clientes")
plt.show()
# plt.savefig("./results.png")
