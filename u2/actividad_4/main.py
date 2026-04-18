# %%
# Imports
import numpy as np
import pandas as pd

# %%
# Ejercicio 1

data = np.arange(10, 130, 10)
print(data)
print("Dim: ", data.shape)
print("Data type: ", data.dtype)
reshaped = data.reshape(4, 3)
print(reshaped)

# %%
# Ejercicio 2

df = pd.DataFrame(reshaped)
avg_by_team = df.mean(axis="columns")
total_avg = avg_by_team.mean()

best_team = np.argmax(avg_by_team)

print("Promedio por equipo:\n", avg_by_team)
print("Promedio total:", total_avg)
print("Mejor equipo:", best_team)

# %%
# Ejercicio 3

above_avg = df[df > total_avg]
above_avg = above_avg.fillna(0)

print(above_avg)

zero_count = (above_avg == 0.0).sum().sum()
print("Numero de resultados afectados", zero_count)

# %%
# Ejercicio 4

random_data = np.random.randint(1, 151, size=df.shape)
random_df = pd.DataFrame(random_data, columns=df.columns)


print(random_df)

total_ran_avg = random_df.mean().mean()
print("Average new random mean", total_ran_avg)

# %%
# Ejercicio 5

data = {
    "ID": [1, 2, 3, 4, 5],
    "Nombre": ["Ana", "Luis", "Marta", "Juan", "Sofia"],
    "Departamento": ["TI", "Ventas", "TI", "RRHH", "Ventas"],
    "Edad": [29, 35, 28, 40, 30],
    "Salario": [1200, 1000, 1300, 900, 1100],
}

df = pd.DataFrame(data)
print(df.dtypes)
(df.describe())

# %%
# Ejercicio 6

df.loc[len(df)] = [np.nan, np.nan, np.nan, np.nan, np.nan]

df = df.fillna({"Edad": df["Edad"].mean(), "Salario": df["Salario"].mean()})
print(df)

# %%
# Ejercicio 7

grouped_by_departamento = df.groupby("Departamento")
print("Salario promedio por departamento\n", grouped_by_departamento["Salario"].mean())
print("Cantidad personas por departamento\n", grouped_by_departamento["ID"].size())


# %%
# Ejercicio 8


def nivel_salarial(salario):
    if salario < 1000:
        return "Bajo"
    elif salario <= 1200:
        return "Medio"
    else:
        return "Alto"


df["Nivel Salarial"] = df["Salario"].apply(nivel_salarial)
print(df)

nivel_salarial_df = df.groupby("Nivel Salarial").size()
print(nivel_salarial_df)

# %%
# Ejercicio 9

bonos_df = pd.DataFrame({"ID": [1, 2, 3, 5], "Bono": [200, 150, 300, 250]})

merged_tables = pd.merge(df, bonos_df, on="ID", how="outer")
merged_tables["Salario total"] = merged_tables["Salario"] + merged_tables["Bono"]
merged_tables

# %%
# Ejercicio 10

avg_per_departamento = merged_tables.groupby("Departamento")["Salario total"].mean()
print(avg_per_departamento)

avg_salario = merged_tables["Salario total"].mean()
print(
    "Salario sobre promedio: ",
    merged_tables[merged_tables["Salario total"] > avg_salario],
)

print("Cantidad personas por departamento\n", grouped_by_departamento["ID"].size())
print("Salario promedio por departamento\n", grouped_by_departamento["Salario"].mean())

print(
    "TI tiene un salario promedio más alto y más personas en el puesto que los demás, por lo tanto, se puede inferir que es el más competitivo"
)
