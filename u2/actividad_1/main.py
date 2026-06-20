# %%
# Imports
from pathlib import Path

import numpy as np
import pandas as pd

# %%
# Crear DataFrame

data = {
    "RUT": [
        "17.432.109-k",
        "15.822.341-5",
        "19.110.457-8",
        "12.654.332-1",
        "18.234.990-4",
        "16.778.223-9",
        "20.443.112-0",
        "14.556.789-2",
        "13.221.445-6",
        "17.990.123-k",
        "15.822.341-5",
        "19.887.654-3",
        "18.234.990-4",
        "18.556.110-2",
        "16.332.998-5",
        "14.990.332-1",
        "21.223.445-0",
        "17.112.887-k",
        "12.998.776-4",
        "18.234.990-4",
        "20.112.554-3",
        "13.887.443-2",
        "18.112.990-k",
        "16.554.112-7",
        np.nan,
        "11.998.112-3",
        "17.554.887-2",
        "14.221.556-9",
        "20.887.332-1",
        "15.667.443-k",
    ],
    "Nombre": [
        "Javiera",
        "Roberto",
        "Camila",
        "Marcos",
        "Elena",
        "Diego",
        "Sofía",
        "Andrés",
        "Patricia",
        "Felipe",
        "Roberto",
        "Nicolás",
        "Elena",
        "Valentina",
        "Gonzalo",
        "Beatriz",
        "Ignacio",
        "Claudia",
        "Jorge",
        "Elena",
        "Matías",
        np.nan,
        "Esteban",
        "Natalia",
        "Gabriel",
        "Luis",
        "Fernanda",
        "Mauricio",
        "Constanza",
        "Rodrigo",
    ],
    "Apellido Paterno": [
        "Alarcón",
        "Muñoz",
        "Rojas",
        "Valenzuela",
        "Castro",
        "Herrera",
        "Morales",
        "Tapia",
        "Lagos",
        "Saavedra",
        "Muñoz",
        "Fuentes",
        "Castro",
        "Núñez",
        "Paredes",
        "Sandoval",
        "Carrasco",
        "Vergara",
        "Henríquez",
        "Castro",
        "Cáceres",
        "Gallardo",
        "Figueroa",
        "Mena",
        "Araya",
        "Pino",
        "Rozas",
        "Olivares",
        "Miranda",
        "Loyola",
    ],
    "Apellido Materno": [
        "Soto",
        "Vera",
        "Espinoza",
        "Pérez",
        "Silva",
        "Martínez",
        "Pardo",
        "González",
        "Vidal",
        "Méndez",
        "Vera",
        "Torres",
        "Silva",
        "Rivas",
        "Jara",
        "Godoy",
        "Peña",
        "Salinas",
        "Ruiz",
        "Silva",
        "Bustos",
        "Reyes",
        "Donoso",
        "Leiva",
        "Farías",
        "Ortiz",
        np.nan,
        "Campos",
        "Villalobos",
        "Maturana",
    ],
    "Edad": [
        29,
        42,
        24,
        55,
        31,
        38,
        22,
        48,
        51,
        28,
        42,
        23,
        31,
        30,
        36,
        46,
        20,
        29,
        53,
        31,
        22,
        49,
        32,
        37,
        25,
        57,
        27,
        47,
        21,
        43,
    ],
    "Sueldo (CLP)": [
        "$850.000",
        "$1.200.000",
        "$650.000",
        "$2.100.000",
        "$980.000",
        "$1.150.000",
        "$520.000",
        np.nan,
        "$1.900.000",
        "$890.000",
        "$1.200.000",
        "$600.000",
        "$980.000",
        "$1.050.000",
        "$1.100.000",
        "$1.550.000",
        "$480.000",
        "$920.000",
        "$2.050.000",
        "$980.000",
        "$550.000",
        "$1.800.000",
        "$1.120.000",
        "$1.180.000",
        "$720.000",
        "$2.250.000",
        "$870.000",
        "$1.680.000",
        "$500.000",
        "$1.420.000",
    ],
}

df = pd.DataFrame(data)
print(df)

# %%
# Preparar los datos

print("Primeras filas:")
print(df.head())
print("Tipos de datos:")
print(df.dtypes)
print("Resumen estadístico:")
print(df.describe())

print("Valores nulos por columna:")
print(df.isnull().sum())

print("Cantidad de filas duplicadas:", df.duplicated().sum())
df = df.drop_duplicates()

df["Sueldo"] = (
    df["Sueldo (CLP)"]
    .astype("string")
    .str.replace("$", "", regex=False)
    .str.replace(".", "", regex=False)
)
df["Sueldo"] = pd.to_numeric(df["Sueldo"], errors="coerce")

df["Nombre Completo"] = (
    df[["Nombre", "Apellido Paterno", "Apellido Materno"]].fillna("").agg(" ".join, axis=1)
)
df["Nombre Completo"] = df["Nombre Completo"].str.replace("  ", " ").str.strip()

print("DataFrame limpio:")
print(df)

# %%
# Lista de personas mayores de 40 años que ganan más de $1.500.000

personas_mayores_40_sueldo_alto = df[(df["Edad"] > 40) & (df["Sueldo"] > 1500000)]

print("Personas mayores de 40 años que ganan más de $1.500.000:")
print(personas_mayores_40_sueldo_alto)

# %%
# Listado del nombre completo de los trabajadores

print("Nombre completo de los trabajadores:")
print(df["Nombre Completo"])

# %%
# Bono para cada trabajador, equivalente a un 25% de su sueldo

df["Bono"] = df["Sueldo"] * 0.25

print("Bono para cada trabajador:")
print(df[["Nombre Completo", "Sueldo", "Bono"]])

# %%
# Guardar datos en CSV

output_path = Path(__file__).with_name("trabajadores_limpios.csv")
df.to_csv(output_path, index=False)

print("Archivo guardado en:", output_path)
