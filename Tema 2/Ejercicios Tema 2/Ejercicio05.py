import pandas as pd

ruta = r"C:\Users\Emiliano\Desktop\vsCode\ERD\ERD\Tema 2\Ejercicios Tema 2\temperaturas.csv"
df = pd.read_csv(ruta)

print("Datos originales:\n", df, "\n")


df = df.dropna(subset=["Temperatura"])


df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
df["Temperatura"] = df["Temperatura"].astype(float)


df["Año"] = df["Fecha"].dt.year
df["Mes"] = df["Fecha"].dt.month
df["Categoría"] = df["Temperatura"].apply(
    lambda t: "Caluroso" if t >= 20 else ("Templado" if t >= 10 else "Frío")
)

exit = r"C:\Users\Emiliano\Desktop\vsCode\ERD\ERD\Tema 2\Ejercicios Tema 2\temperaturas_limpias.csv"
df.to_csv(exit, index=False, encoding="utf-8-sig")

print("Datos limpios y transformados:\n", df, "\n")
print(f"Archivo exportado en:\n{exit}")
