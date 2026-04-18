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
