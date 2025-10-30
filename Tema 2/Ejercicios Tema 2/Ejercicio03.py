import pandas as pd

# Ruta base (ajustala si hace falta)
df = r"C:\Users\Emiliano\Desktop\vsCode\ERD\ERD\Tema 2\Ejercicios Tema 2"

# Leer los CSV
students = pd.read_csv(df + r"\alumnos.csv")
notes = pd.read_csv(df + r"\notas.csv")

# Limpiar datos (quitar filas vacías)
students_clean = students.dropna()

# Guardar el limpio.csv
students_clean.to_csv(df + r"\limpio.csv", index=False)

# Unir los dos DataFrames por la columna 'nombre'
complete = pd.merge(students_clean, notes, on="nombre", how="inner")

# Mostrar resultados
print("Alumnos:")
print(students_clean.head(), "\n")

print("Notas:")
print(notes.head(), "\n")

print("Merge completo:")
print(complete.head())