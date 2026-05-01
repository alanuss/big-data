# %%

# Parte 1:
import numpy as np

desempeno = np.array([80, 90, 75, 85, 60, 70, 65, 75, 95, 85, 90, 100])

# %%
# 1
reorganizada = desempeno.reshape(3, 4)
print("Matriz reorganizada (3 equipos, 4 meses):")
print(reorganizada)


# %%
# 2
promedio_por_equipo = reorganizada.mean(axis=1)
print("Promedio de desempeño por equipo:")
print(promedio_por_equipo)

promedio_por_mes = reorganizada.mean(axis=0)
print("Promedio de desempeño por mes:")
print(promedio_por_mes)

promedio_general = reorganizada.mean()
print("Promedio general de desempeño:")
print(promedio_general)

# %%
# 3

idx_mejor_equipo = np.argmax(promedio_por_equipo)
print(
    f"El equipo con mejor desempeño promedio es el Equipo {idx_mejor_equipo + 1} con un promedio de {promedio_por_equipo[idx_mejor_equipo]}"
)

idx_mejor_mes = np.argmax(promedio_por_mes)
print(
    f"El mes con mejor desempeño promedio es el Mes {idx_mejor_mes + 1} con un promedio de {promedio_por_mes[idx_mejor_mes]}"
)

# %%
# 4

sobre_promedio_general = reorganizada[reorganizada > promedio_general]
print("Desempeños individuales sobre el promedio general:")
print(sobre_promedio_general)

replace_valores_bajo_70 = reorganizada.copy()
replace_valores_bajo_70[replace_valores_bajo_70 < 70] = 0
print("Matriz con valores bajo 70 reemplazados por 0:")
print(replace_valores_bajo_70)

# %%
# Parte 2:

import pandas as pd

df = pd.DataFrame(
    {
        "ID": [1, 2, 3, 4, 5, 6],
        "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Silla", "Escritorio"],
        "Categoria": [
            "Tecnología",
            "Tecnología",
            "Tecnología",
            "Tecnología",
            "Hogar",
            "Hogar",
        ],
        "Precio": [800, 20, 50, 300, 120, 250],
        "Cantidad": [5, 50, 30, 10, 15, 8],
        "Sucursal": ["Norte", "Sur", "Centro", "Norte", "Sur", "Centro"],
    }
)

# %%
# 1
df["Ingreso"] = df["Precio"] * df["Cantidad"]

# %%
# 2
ingreso_total_categoria = df.groupby("Categoria")["Ingreso"].sum()
ingreso_total_sucursal = df.groupby("Sucursal")["Ingreso"].sum()

print("Ingreso total por categoría:")
print(ingreso_total_categoria)

print("Ingreso total por sucursal:")
print(ingreso_total_sucursal)

# %%
# 3

promedio_por_producto = df.groupby("Producto")["Ingreso"].mean()
cantidad_total_vendida = df.groupby("Producto")["Cantidad"].sum()

print("Promedio de ingreso por producto:")
print(promedio_por_producto)
print("Cantidad total vendida por producto:")
print(cantidad_total_vendida)

# %%
# 4


def nivel_venta(venta: int):
    if venta >= 3000:
        return "Alta"
    elif venta >= 1000:
        return "Media"
    else:
        return "Baja"


df["Nivel_Venta"] = df["Ingreso"].apply(nivel_venta)
print(df)

# %%
# 5

avg = df["Ingreso"].mean()
sobre_promedio = df[df["Ingreso"] > avg]
print(f"Productos con ingreso sobre el promedio ({avg}):")
print(sobre_promedio[["Producto", "Ingreso"]])
