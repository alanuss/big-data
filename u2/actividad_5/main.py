# %%
# Imports
import numpy as np
import pandas as pd

# %%
# Parte 1

ventas = np.array([120, 150, 90, 200, 80, 110, 140, 170, 100, 130, 160, 180])

# %%
# Ejercicio 1

print("Dimensión del arreglo:", ventas.shape)
print("Tipo de dato:", ventas.dtype)

matriz_ventas = ventas.reshape(3, 4)
print("Matriz de ventas:")
print(matriz_ventas)
print("Cada fila representa una sucursal y cada columna representa un mes")

# %%
# Ejercicio 2

ventas_totales_sucursal = matriz_ventas.sum(axis=1)
ventas_promedio_mes = matriz_ventas.mean(axis=0)

print("Ventas totales por sucursal:")
print(ventas_totales_sucursal)
print("Ventas promedio por mes:")
print(ventas_promedio_mes)

idx_mejor_sucursal = np.argmax(ventas_totales_sucursal)
idx_mejor_mes = np.argmax(ventas_promedio_mes)

print(
    f"La sucursal con mayores ventas totales es la Sucursal {idx_mejor_sucursal + 1} con {ventas_totales_sucursal[idx_mejor_sucursal]}"
)
print(
    f"El mes con mayores ventas promedio es el Mes {idx_mejor_mes + 1} con {ventas_promedio_mes[idx_mejor_mes]}"
)

# %%
# Ejercicio 3

promedio_general = matriz_ventas.mean()
print("Promedio general de ventas:", promedio_general)

ventas_sobre_promedio = matriz_ventas[matriz_ventas > promedio_general]
print("Ventas superiores al promedio general:")
print(ventas_sobre_promedio)

ventas_bajo_rendimiento = matriz_ventas.copy()
ventas_bajo_rendimiento[ventas_bajo_rendimiento < 100] = 0
print("Matriz con ventas menores a 100 reemplazadas por 0:")
print(ventas_bajo_rendimiento)

# %%
# Ejercicio 4

nuevo_periodo = np.random.randint(80, 201, size=matriz_ventas.shape)
diferencia_periodos = nuevo_periodo - matriz_ventas

print("Ventas de nuevo periodo:")
print(nuevo_periodo)
print("Diferencia entre periodos:")
print(diferencia_periodos)

promedio_diferencia = diferencia_periodos.mean()
print("Promedio de diferencia:", promedio_diferencia)

if promedio_diferencia > 0:
    print("En promedio las ventas aumentaron")
elif promedio_diferencia < 0:
    print("En promedio las ventas disminuyeron")
else:
    print("En promedio las ventas se mantuvieron iguales")

# %%
# Parte 2

df = pd.DataFrame(
    {
        "ID": [1, 2, 3, 4, 5],
        "Producto": ["Laptop", "Mouse", "Silla", "Escritorio", "Audífonos"],
        "Categoria": ["Tecnología", "Tecnología", "Hogar", "Hogar", "Tecnología"],
        "Precio": [800, 20, 100, 200, 50],
        "Cantidad": [5, 50, 10, 7, 20],
    }
)

# %%
# Ejercicio 5

df["Ingreso"] = df["Precio"] * df["Cantidad"]
print(df)

# %%
# Ejercicio 6

ingreso_total_categoria = df.groupby("Categoria")["Ingreso"].sum()
cantidad_total_categoria = df.groupby("Categoria")["Cantidad"].sum()

print("Ingreso total por categoría:")
print(ingreso_total_categoria)
print("Cantidad total vendida por categoría:")
print(cantidad_total_categoria)

categoria_mas_rentable = ingreso_total_categoria.idxmax()
print("Categoría más rentable:", categoria_mas_rentable)

# %%
# Ejercicio 7


def nivel_venta(ingreso: int):
    if ingreso > 2000:
        return "Alto"
    elif ingreso >= 500:
        return "Medio"
    else:
        return "Bajo"


df["Nivel_Venta"] = df["Ingreso"].apply(nivel_venta)
print(df)

productos_por_nivel = df.groupby("Nivel_Venta").size()
print("Productos por nivel de venta:")
print(productos_por_nivel)

# %%
# Ejercicio 8

ingreso_promedio = df["Ingreso"].mean()
print("Ingreso promedio:", ingreso_promedio)

productos_sobre_promedio = df[df["Ingreso"] > ingreso_promedio]
productos_sobre_promedio = productos_sobre_promedio.sort_values("Ingreso", ascending=False)

print("Productos con ingreso superior al promedio:")
print(productos_sobre_promedio)

# %%
# Ejercicio 9

sucursales_df = pd.DataFrame(
    {
        "ID": [1, 2, 3, 4, 5],
        "Sucursal": ["Norte", "Sur", "Centro", "Norte", "Sur"],
    }
)

merged_tables = pd.merge(df, sucursales_df, on="ID")
print(merged_tables)

ingreso_total_sucursal = merged_tables.groupby("Sucursal")["Ingreso"].sum()
print("Ingreso total por sucursal:")
print(ingreso_total_sucursal)

# %%
# Ejercicio 10

mejor_sucursal = ingreso_total_sucursal.idxmax()
print("Sucursal con mayor ingreso:", mejor_sucursal)

ingreso_categoria_sucursal = (
    merged_tables.groupby(["Sucursal", "Categoria"])["Ingreso"].sum().reset_index()
)
categorias_dominantes = ingreso_categoria_sucursal.loc[
    ingreso_categoria_sucursal.groupby("Sucursal")["Ingreso"].idxmax()
]

print("Categoría dominante en cada sucursal:")
print(categorias_dominantes)

alto_rendimiento_mejor_sucursal = merged_tables[
    (merged_tables["Sucursal"] == mejor_sucursal) & (merged_tables["Nivel_Venta"] == "Alto")
]

print("Productos con alto rendimiento en la mejor sucursal:")
print(alto_rendimiento_mejor_sucursal)
