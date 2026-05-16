import numpy as np
import pandas as pd


def generar_datos_a_csv(n=1000, random_seed=57, csv_filename="datos_salud.csv"):
    np.random.seed(random_seed)

    datos = {
        "ID": range(1, n + 1),
        "Edad": np.random.randint(18, 81, n),
        "Ciudad": np.random.choice(
            ["Puerto Varas", "Puerto Montt", "Llanquihue", "Concepción", "Temuco"], n
        ),
        "HorasEjercicio": np.round(np.random.uniform(0, 10, n), 1),
        "IMC": np.round(np.random.uniform(15, 40, n), 1),
        "Fuma": np.random.choice(["Sí", "No"], n),
        "Consumo": np.random.choice(["Pescado", "Verduras", "Frutas"], n),
    }

    df = pd.DataFrame(datos)
    df.to_csv(csv_filename, index=False, encoding="utf-8")


if __name__ == "__main__":
    generar_datos_a_csv()
