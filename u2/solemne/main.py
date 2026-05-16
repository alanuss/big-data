# %%
# Importar las librerías necesarias (EJERCICIO 1)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from generar_datos import generar_datos_a_csv

# %%
# Generar datos de ejemplo y guardarlos en un archivo CSV (EJERCICIO 1)
generar_datos_a_csv(n=1000, random_seed=57, csv_filename="datos_salud.csv")

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
datos_normalizados = (horas_ejercicio - horas_ejercicio.min()) / (
    horas_ejercicio.max() - horas_ejercicio.min()
)  # Min Max scaler. Numpy no trae este por defecto como skilearn :(
