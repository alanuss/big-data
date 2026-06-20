# %%
# Imports
import numpy as np
import pandas as pd

# %%
# Parte 1
# Ejercicio 1

arr = np.arange(1, 21)
print(arr)
print("Shape:", arr.shape)
print("Data type:", arr.dtype)

matriz = arr.reshape(4, 5)
print(matriz)

segunda_fila = matriz[1]
tercera_columna = matriz[:, 2]

print("Segunda fila:", segunda_fila)
print("Tercera columna:", tercera_columna)

# %%
# Ejercicio 2

arr = np.array([5, 10, 15, 20, 25, 30])
arr = arr * 3
print("Valores multiplicados por 3:")
print(arr)

arr[arr > 20] = -1
print("Valores mayores a 20 reemplazados por -1:")
print(arr)

valores_positivos = arr[arr > 0]
print("Valores positivos resultantes:")
print(valores_positivos)

# %%
# Ejercicio 3

matriz_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

suma_matrices = matriz_a + matriz_b
multiplicacion_matrices = matriz_a * matriz_b

print("Suma entre matrices:")
print(suma_matrices)
print("Multiplicación elemento a elemento:")
print(multiplicacion_matrices)

print("Suma total matriz A:", matriz_a.sum())
print("Suma total matriz B:", matriz_b.sum())

# %%
# Ejercicio 4

arr = np.random.randint(1, 50, size=10)
print(arr)

promedio = arr.mean()
maximo = arr.max()
minimo = arr.min()
ordenado = np.sort(arr)
mayores_promedio = arr[arr > promedio]

print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Arreglo ordenado:")
print(ordenado)
print("Cantidad de valores mayores al promedio:", len(mayores_promedio))

# %%
# Ejercicio 5

matriz_random = np.random.randint(1, 101, size=(5, 4))
promedio_por_fila = matriz_random.mean(axis=1)
idx_mayor_promedio = np.argmax(promedio_por_fila)

print("Matriz aleatoria:")
print(matriz_random)
print("Promedio por fila:")
print(promedio_por_fila)
print("Fila con mayor promedio:", idx_mayor_promedio)
print(matriz_random[idx_mayor_promedio])

# %%
# Parte 2
# Ejercicio 6

df = pd.DataFrame(
    {
        "Nombre": ["Ana", "Luis", "Marta", "Juan", "Sofia"],
        "Edad": [20, 22, 21, 23, 19],
        "Carrera": ["Ing", "Med", "Ing", "Med", "Ing"],
    }
)

print("Primeras filas:")
print(df.head())
print("Tipos de datos:")
print(df.dtypes)
print("Resumen estadístico:")
print(df.describe())

# %%
# Ejercicio 7

df["Promedio"] = [5.5, 3.8, 4.7, 6.0, 3.5]
df["Estado"] = np.where(df["Promedio"] >= 4, "Aprobado", "Reprobado")

print(df)

aprobados = df[df["Estado"] == "Aprobado"]
print("Estudiantes aprobados:")
print(aprobados)

# %%
# Ejercicio 8

data = {
    "Carrera": ["Ing", "Ing", "Med", "Med", "Ing"],
    "Promedio": [5.0, 4.5, 6.0, 5.5, 3.8],
}

df_notas = pd.DataFrame(data)
grouped_by_carrera = df_notas.groupby("Carrera")

print("Promedio de notas por carrera:")
print(grouped_by_carrera["Promedio"].mean())
print("Cantidad de estudiantes por carrera:")
print(grouped_by_carrera.size())

# %%
# Ejercicio 9

nuevos_estudiantes = pd.DataFrame(
    {
        "Nombre": ["Pedro", "Camila"],
        "Edad": [24, 20],
        "Carrera": ["Ing", "Med"],
        "Promedio": [4.2, 6.3],
        "Estado": ["Aprobado", "Aprobado"],
    }
)

df = pd.concat([df, nuevos_estudiantes], ignore_index=True)
print(df)

promedio_general = df["Promedio"].mean()
print("Promedio general:", promedio_general)

estudiantes_sobre_promedio = df[df["Promedio"] > promedio_general]
print("Estudiantes sobre el promedio general:")
print(estudiantes_sobre_promedio)

# %%
# Ejercicio 10

df1 = pd.DataFrame(
    {
        "ID": [1, 2, 3, 4],
        "Nombre": ["Ana", "Luis", "Marta", "Juan"],
    }
)

df2 = pd.DataFrame(
    {
        "ID": [1, 2, 3, 5],
        "Carrera": ["Ing", "Med", "Ing", "Med"],
    }
)

merged_tables = pd.merge(df1, df2, on="ID", how="outer", indicator=True)
print(merged_tables)

ids_sin_coincidencia = merged_tables[merged_tables["_merge"] != "both"]
print("IDs sin coincidencia:")
print(ids_sin_coincidencia)
