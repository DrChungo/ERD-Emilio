import pandas as pd
import numpy as np


data = {
    "Nombre": ["Ana", "Marc", "Julia", "Ana", "Pau", None],
    "Edad": [20, None, 22, 20, 21, 23],
    "Nota": [8.5, 7.0, None, 8.5, 9.0, None],
    "Precio": ["12.5", "8.0", "10.0", "12.5", None, "9.5"]
}


df = pd.DataFrame(data)
print("DataFrame inicial:\n", df)


df = df.dropna(how='all')
print("\nDespues de eliminar filas completamente vacías:\n", df)


df['Edad'] = df['Edad'].fillna(df['Edad'].mean())
df['Nota'] = df['Nota'].fillna(df['Nota'].mean())
print("\nDespues de sustituir nulos por la media:\n", df)


df = df.drop_duplicates()
print("\nDespues de eliminar duplicados:\n", df)


df['Precio'] = df['Precio'].astype(float)

df['Precio'] = df['Precio'].fillna(df['Precio'].mean())

print("\nDataFrame con 'Precio' convertido a float:\n", df)

media_precio = df['Precio'].mean()
mean_note= df['Nota'].mean()
print("\nLa media de los precios es:", mean_note)
