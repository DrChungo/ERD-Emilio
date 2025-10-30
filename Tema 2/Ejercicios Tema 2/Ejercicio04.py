import pandas as pd


notes_csv = r"C:\Users\Emiliano\Desktop\vsCode\ERD\ERD\Tema 2\Ejercicios Tema 2\notas.csv"

df = pd.read_csv(notes_csv)


mean = df["Nota"].mean()
max   = df["Nota"].max()
min   = df["Nota"].min()

def cat(n):
    if n >= 9: return "Excelente"
    if n >= 7: return "Notable"
    if n >= 5: return "Suficiente"
    return "Insuficinete"

df["Categoria"] = df["Nota"].apply(cat)

print("Mediana:", mean, "| Maximo:", max, "| Minimo:", min)
print(df.head())

import pandas as pd


ventas_csv = r"C:\Users\Emiliano\Desktop\vsCode\ERD\ERD\Tema 2\Ejercicios Tema 2\ventas.csv"


sales = pd.read_csv(ventas_csv)


sales["Fecha"] = pd.to_datetime(sales["Fecha"], errors="coerce")


sales = sales.dropna(subset=["Fecha"])
sales = sales[sales["Cantidad"] > 0]


sales["Importe"] = sales["Cantidad"] * sales["Precio"]


total = sales.groupby("Producto", as_index=False)["Importe"].sum()

# Mostrar el resultado
print("Totales de ventas por producto:")
print(total)
